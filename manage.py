#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    target = 'development'
    if os.path.isfile('.target'):
        target = open('.target', 'r').readline().strip()
        if not target or not os.path.isfile('casevo/settings/%s.py' % target):
            sys.exit("Unknown target '%s'" % target)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evolin.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
