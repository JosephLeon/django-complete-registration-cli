from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
            parser.add_argument('app_name')

    def handle(self, *args, **options):
        test = 'Command worked'
        # argument = options['app_name']
        # self.stdout.write(options)
        print options
        try:

            # print argument
            # print test
            self.stdout.write(test)
            # print app_name
        except test.DoesNotExist:
            raise CommandError("Test doesn't exist.")
