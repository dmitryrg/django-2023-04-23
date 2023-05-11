from django.core.management.base import BaseCommand
import json

from school.models import Teacher, Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=str)

    def handle(self, *args, **options):
        with open(options['filename'][0], 'r', encoding='utf-8') as file:
            records = json.load(file)

        for record in records:
            if record['model'] == 'school.teacher':
                try:
                    Teacher.objects.get(id=record['pk'])
                except:
                    Teacher.objects.create(
                        id=record['pk'],
                        name=record['fields']['name'],
                        subject=record['fields']['subject']
                    )
            elif record['model'] == 'school.student':
                try:
                    Student.objects.get(id=record['pk'])
                except:
                    teacher = Teacher.objects.get(id=record['fields']['teacher'])
                    Student.objects.create(
                        id=record['pk'],
                        name=record['fields']['name'],
                        group=record['fields']['group'],
                        teacher=teacher
                    )
        print('Base fill')



