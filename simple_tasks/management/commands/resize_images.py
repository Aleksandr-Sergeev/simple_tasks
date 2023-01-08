from django.core.management.base import BaseCommand
from files.operations.resize_images_async import resize_images
# from files.operations.resize_images_sync import resize_images


class Command(BaseCommand):
    help = 'Builds tree based on predefined graph'

    def add_arguments(self, parser):
        parser.add_argument('--source', '-s', type=str, action='store', dest='source', required=True)
        parser.add_argument('--resize_percent', '-percent', type=str, action='store', dest='resize_percent', required=True)
        parser.add_argument('--async', '-as', type=bool, action='store', dest='async', default=True)

    def handle(self, *args, **options):
        images_source = options.get('source')
        resize_percent = options.get('resize_percent')
        do_async = options.get('async')
        resize_images(source=images_source, resize_percent=resize_percent, do_async=do_async)

    def _fail(self, message, code=1):
        self.stderr.write(message)
        exit(code)