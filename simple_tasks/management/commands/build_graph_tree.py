import os
from django.conf import settings
from django.core.management.base import BaseCommand
from simple_tasks.management.actions.build_graph_tree import to_tree, source


class Command(BaseCommand):
    help = 'Builds tree based on predefined graph'

    def handle(self, *args, **options):
        page_content = to_tree(source)
        counter_function = None

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)