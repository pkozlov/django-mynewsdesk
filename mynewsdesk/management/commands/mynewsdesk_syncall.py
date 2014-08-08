from django.core.management.base import BaseCommand, CommandError
from mynewsdesk import sync

class Command(BaseCommand):
    def handle(self, *args, **options):
        r = sync.sync_all()
        print r