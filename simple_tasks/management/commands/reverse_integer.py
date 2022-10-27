import os
from django.conf import settings
from django.core.management.base import BaseCommand
from simple_tasks.management.actions.reverse_integer import Solution


class Command(BaseCommand):
    help = 'Builds tree based on predefined graph'

    def handle(self, *args, **options):
        Solution.reverse()

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)