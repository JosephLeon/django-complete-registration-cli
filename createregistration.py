from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        test = 'Command worked'
        try:
            print test
        except test.DoesNotExist:
            raise CommandError("Test doesn't exist.")
