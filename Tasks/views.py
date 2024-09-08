from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.db.models import Q
import datetime
from .forms import TaskForm
from django.contrib import messages


def task_list(request):
    """
    View function for listing tasks.
    """
    # getting all tasks
    tasks = Task.objects.all()
    total_tasks = tasks.count()

    # getting filters from url
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    due_date = request.GET.get('due_date')
    search = request.GET.get('search')

    # applying filters to tasks
    # using Q objects for searching
    if search:
        tasks = tasks.filter(Q(title__icontains=search) |
                             Q(description__icontains=search))
    if status:
        tasks = tasks.filter(status=status)

    if priority:
        tasks = tasks.filter(priority=priority)

    if due_date:
        tasks = tasks.filter(due_date=due_date)

    # getting task which are due today and whose status is not done
    # this can be used to show how much tasks are due today in alert message
    today = datetime.date.today()
    tasks_due_today = tasks.filter(Q(due_date=today) & ~Q(status="DONE"))
    num_of_tasks_due_today = tasks_due_today.count()

    # only show message when all the tasks are fetched not when a filter is applied
    if tasks.count() == total_tasks:
        messages.info(request, 'Tasks due today: ' +
                      str(num_of_tasks_due_today))

    context = {
        'tasks': tasks,
        'status': status,
        'priority': priority,
        'due_date': due_date,
        'search': search,
        'num_of_tasks_due_today': num_of_tasks_due_today
    }
    return render(request, 'task_list.html', context)


# this tasks_due_today view is currently unused
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


def create_task(request):
    """
    View function for creating tasks.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully')
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form, })


def update_task(request, pk):
    """
    View function for updating tasks.
    """
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully')
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form, })


def delete_task(request, pk):
    """
    View function for deleting tasks.
    """
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.success(request, 'Task deleted successfully')
    return redirect('task-list')
