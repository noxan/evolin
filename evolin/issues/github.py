import logging

from github import Github

from django.conf import settings

from evolin.issues.settings import ISSUES_GITHUB_STATE_MAPPING
from evolin.issues.models import Issue, IssueState
from evolin.projects.models import Project


logger = logging.getLogger(__name__)


def sync_issues(github_project_name):
    owner, name = github_project_name.split('/')

    g = Github(settings.GITHUB_OAUTH_TOKEN)

    repo = g.get_repo(github_project_name)

    project = Project.objects.get(owner__username=owner, name=name)

    logger.info("Importing all new issues for project '%s'." % project.full_name)

    project_import_count = 0

    for state in ISSUES_GITHUB_STATE_MAPPING.keys():
        for github_issue in repo.get_issues(state=state):
            issuestate = IssueState.objects.get(pk=ISSUES_GITHUB_STATE_MAPPING[state])
            issue, created = Issue.objects.get_or_create(project=project, number=github_issue.number, defaults={
                'title': github_issue.title,
                'body': github_issue.body,
                'created_at': github_issue.created_at,
                'updated_at': github_issue.updated_at,
                'state': issuestate,
            })
            if created:
                logger.info("Imported new issue '%s'." % (issue))
                project_import_count += 1
            else:
                logger.debug("Skipped issue '%s' because it has already been imported." % (issue))

    logger.info("Imported %d new issues for project '%s'." % (project_import_count, project.full_name))
