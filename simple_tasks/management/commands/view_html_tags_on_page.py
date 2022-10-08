import os
from django.conf import settings
from django.core.management.base import BaseCommand
from simple_tasks.management.actions.count_html_tags_on_page import get_page_content


class Command(BaseCommand):
    """
    Подсчет количества HTML-Tags на веб-странице:
    1. всего html-tags
    2. html-tags с атрибутами
    """
    help = 'Count html-tags on a web-page'

    def add_arguments(self, parser):
        parser.add_argument('--url', type=str, action='store', dest='source_url', required=True)

    def handle(self, *args, **options):
        source_url = options.get('source_url')
        page_content = get_page_content(source_url=source_url)
        counter_function = None

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)