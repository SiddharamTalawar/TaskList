from django.urls import path
from Tasks.views import task_list, search_task_list

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('search/', search_task_list, name='search-task-list'),

]
