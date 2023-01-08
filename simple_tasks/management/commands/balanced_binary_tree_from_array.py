import os
from django.conf import settings
from django.core.management.base import BaseCommand
from trees.operations.balanced_binary_tree_from_array import Solution


class Command(BaseCommand):
    help = 'Builds tree based on predefined graph'

    def handle(self, *args, **options):
        Solution.balanced_binary_tree_from_array()

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)