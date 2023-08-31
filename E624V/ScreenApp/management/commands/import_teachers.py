import csv
from django.core.management.base import BaseCommand
from ScreenApp.models import Teacher

class Command(BaseCommand):
    help = 'Import teachers from CSV'
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')
    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                teacher = Teacher(
                    name=row['Name'],
                    identity=row['Title'],
                    department=row['Department'],
                )
                teacher.save()
        self.stdout.write(self.style.SUCCESS('Data import complete'))
