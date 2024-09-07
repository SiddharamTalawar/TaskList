from django.shortcuts import render
from .models import Task
from django.db.models import Q
import datetime


def task_list(request):
    """
    View function for listing tasks.
    """
    tasks = Task.objects.all()
    # print("not filterd tasks.....", tasks)
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    due_date = request.GET.get('due_date')
    search = request.GET.get('search')
    # print("................", status, priority, due_date, search)

    # applying filters
    if search:
        tasks = tasks.filter(Q(title__icontains=search) |
                             Q(description__icontains=search))
    if status:
        tasks = tasks.filter(status=status)

    if priority:
        tasks = tasks.filter(priority=priority)

    if due_date:
        tasks = tasks.filter(due_date=due_date)
    # print("filterd tasks.....", tasks)
    context = {
        'tasks': tasks,
        'status': status,
        'priority': priority,
        'due_date': due_date,
        'search': search,

    }
    return render(request, 'task_list.html', context)


def search_task_list(request):
    tasks = Task.objects.all()
    query = request.GET.get('search')
    if query:
        tasks = tasks.filter(title__icontains=query)
    else:
        tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
