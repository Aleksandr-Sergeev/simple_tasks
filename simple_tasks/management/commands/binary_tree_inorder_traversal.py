import os
from django.conf import settings
from django.core.management.base import BaseCommand
from trees.core.binary_tree import BalancedTree


class Command(BaseCommand):
    help = 'Builds tree based on predefined graph'

    def handle(self, *args, **options):
        balanced_tree = BalancedTree.generate_random_balanced_tree()
        balanced_tree.inorder_traversal_list()

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)