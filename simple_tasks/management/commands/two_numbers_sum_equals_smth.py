import os
from django.conf import settings
from django.core.management.base import BaseCommand
from simple_tasks.management.actions.two_numbers_sum_equals_smth import Solution


class Command(BaseCommand):
    help = 'Builds tree based on predefined graph'

    def handle(self, *args, **options):
        Solution.two_sum()

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)