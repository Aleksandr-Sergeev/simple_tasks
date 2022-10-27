import os
from django.conf import settings
from django.core.management.base import BaseCommand
from simple_tasks.management.actions.get_target_str import Solution


class Command(BaseCommand):
    help = 'Builds tree based on predefined graph'

    def handle(self, *args, **options):
        Solution.get_target_str()

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)