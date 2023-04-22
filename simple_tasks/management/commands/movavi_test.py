import os
from django.conf import settings
from django.core.management.base import BaseCommand
from simple_tasks.management.actions import movavi_test_solution


class Command(BaseCommand):
    help = 'Builds tree based on predefined graph'

    def add_arguments(self, parser):
        parser.add_argument('--data_loc', type=str, action='store', dest='data_loc', required=True)

    def handle(self, *args, **options):
        data_loc = options.get('data_loc')
        movavi_solution_instance = movavi_test_solution.Solution(data_loc=data_loc)
        movavi_solution_instance.execute()

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)