from django.shortcuts import render
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    status = request.GET.get('status')
    sort_by = request.GET.get('sort_by')

    if status:
        tasks = tasks.filter(status=status)
    if sort_by:
        tasks = tasks.order_by(sort_by)

    return render(request, 'task_list.html', {'tasks': tasks})
