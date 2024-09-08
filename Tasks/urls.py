from django.urls import path
from Tasks.views import task_list, tasks_due_today, create_task, update_task, delete_task

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('tasks-due-today/', tasks_due_today, name='tasks-due-today'),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:pk>/', update_task, name='update-task'),
    path('delete-task/<int:pk>/', delete_task, name='delete-task'),

]
