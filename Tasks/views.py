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

    # getting task which are due today and whose status is not done
    today = datetime.date.today()
    tasks_due_today = tasks.filter(Q(due_date=today) & ~Q(status="DONE"))
    num_of_tasks_due_today = tasks_due_today.count()
    # print("todays tasks.....", todays_tasks.count())

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
        'num_of_tasks_due_today': num_of_tasks_due_today
    }
    return render(request, 'task_list.html', context)


def tasks_due_today(request):
    """
    View function for listing tasks due today.
    """
    tasks = Task.objects.all()
    today = datetime.date.today()
    tasks_due_today = tasks.filter(Q(due_date=today) & ~Q(status="DONE"))
    uncompleted_tasks = tasks.filter(~Q(status="DONE"))
    num_of_tasks_due_today = tasks_due_today.count()
    context = {
        'tasks': tasks_due_today,
        'num_of_tasks_due_today': num_of_tasks_due_today,
        'msg': 'Tasks due today'
    }
    return render(request, 'task_list.html', context)
