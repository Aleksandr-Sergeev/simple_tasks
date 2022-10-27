import os
from django.conf import settings
from django.core.management.base import BaseCommand
from simple_tasks.management.actions.break_palindrome import break_palindrome, palindrome


class Command(BaseCommand):
    help = 'Builds tree based on predefined graph'

    def handle(self, *args, **options):
        break_palindrome(palindrome)

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)