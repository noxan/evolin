from django.core.management.base import BaseCommand, CommandError

from evolin.issues.github import sync_issues


class Command(BaseCommand):
    def handle(self, *args, **options):
        if len(args) < 1 or '/' not in args[0]:
            raise CommandError("you must provide a github project path <owner/project>")

        sync_issues(args[0])
