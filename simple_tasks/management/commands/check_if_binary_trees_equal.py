import os
from django.conf import settings
from django.core.management.base import BaseCommand
from trees.core.binary_tree import BalancedTree
from trees.operations.check_if_binary_trees_equal import check_if_binary_trees_equal


class Command(BaseCommand):
    help = 'Builds tree based on predefined graph'

    def handle(self, *args, **options):
        tree_one = BalancedTree.generate_random_balanced_tree()
        tree_two = BalancedTree.generate_random_balanced_tree()
        check_if_binary_trees_equal(tree_one, tree_two)

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)