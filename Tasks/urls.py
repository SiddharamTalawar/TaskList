from django.urls import path
from Tasks.views import task_list, tasks_due_today

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('tasks-due-today/', tasks_due_today, name='tasks-due-today'),

]
