from django.core.management.base import BaseCommand
import csv
from kickstarterapp.models import Kickstarter

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='{Path to csv}')

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']
        print(f'The total is {file_path}')

        # Reading a CSV
        with open(file_path, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if(line_count != 0):
                    Kickstarter.objects.create(
                        backers_count = row[0],
                        blurb = row[1],
                        category = row[2]
                    )
                line_count += 1

#Kickstarter.objects.create(
#    backers_count = row[0],
#    blurb = row[1],
#    category = row[2]
#)
