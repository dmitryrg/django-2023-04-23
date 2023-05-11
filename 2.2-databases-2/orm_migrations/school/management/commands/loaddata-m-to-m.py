from django.core.management.base import BaseCommand
import json

from school.models import Teacher, Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('school.json', 'r', encoding='utf-8') as file:
            records = json.load(file)

        for record in records:
            if record['model'] == 'school.teacher':
                try:
                    teacher = Teacher.objects.get(id=record['pk'])
                except:
                    teacher = Teacher.objects.create(
                        id=record['pk'],
                        name=record['fields']['name'],
                        subject=record['fields']['subject']
                    )
            elif record['model'] == 'school.student':
                try:
                    student = Student.objects.get(id=record['pk'])
                except:
                    student = Student.objects.create(
                        id=record['pk'],
                        name=record['fields']['name'],
                        group=record['fields']['group']
                    )
                # при добавлении связи, если уже существует, то просто игнорирует команду, ошибки нет
                student.teachers.add(teacher)


        print('Base fill')



