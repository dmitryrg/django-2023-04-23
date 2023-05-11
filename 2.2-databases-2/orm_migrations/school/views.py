# from django.views.generic import ListView
from django.shortcuts import render

from school.models import Teacher, Student


def students_list(request):
    template = 'school/students_list.html'

    students = Student.objects.select_related('teacher').all()
#     { %
#     for student in object_list %}
#     < li > {{student.name}}
#     {{student.group}} < br > Преподаватель: {{student.teacher.name}}
#     {{student.teacher.subject}} < / li >
# { % endfor %}
    object_list = []
    for student in students:
        object_list.append({
            'name': student.name,
            'group': student.group,
            'teacher': {
                'name': student.teacher.name,
                'subject': student.teacher.subject
            }
        })

    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
