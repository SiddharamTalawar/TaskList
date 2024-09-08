from django.test import TestCase
from .models import Task
import datetime
from django.urls import reverse


class TaskListViewTests(TestCase):
    def setUp(self):
        Task.objects.create(title="Task 1", description="Task 1 description",
                            due_date="2024-09-10", priority=1, status="To Do")
        Task.objects.create(title="Task 2", description="Task 2 description",
                            due_date="2024-09-11", priority=2, status="In Progress")

    def test_all_tasks(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")

    def test_filter_by_status(self):
        response = self.client.get('/tasks/?status=To Do')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 1")
        self.assertNotContains(response, "Task 2")

    def test_filter_by_priority(self):
        response = self.client.get('/tasks/?priority=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 1")
        self.assertNotContains(response, "Task 2")

    def test_filter_by_due_date(self):
        response = self.client.get('/tasks/?due_date=2024-09-10')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 1")
        self.assertNotContains(response, "Task 2")

    def test_search_by_title(self):
        response = self.client.get('/tasks/?search=Task 1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 1")
        self.assertNotContains(response, "Task 2")

    def test_search_by_description(self):
        response = self.client.get('/tasks/?search=Task 2')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 2")
        self.assertNotContains(response, "Task 1")


class TasksDueTodayViewTests(TestCase):
    def setUp(self):
        Task.objects.create(title="Task 1", description="Task 1 description",
                            due_date=datetime.date.today(), priority=1, status="To Do")
        Task.objects.create(title="Task 2", description="Task 2 description",
                            due_date="2024-09-11", priority=2, status="In Progress")

    def test_tasks_due_today(self):
        response = self.client.get('/tasks-due-today/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 1")
        self.assertNotContains(response, "Task 2")

    def test_num_of_tasks_due_today(self):
        response = self.client.get('/tasks-due-today/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['num_of_tasks_due_today'], 1)


class CreateTaskViewTests(TestCase):
    def test_create_task(self):
        response = self.client.post(reverse('create-task'), {
            'title': 'New Task',
            'description': 'New Description',
            'due_date': '2024-09-15',
            'priority': 1,
            'status': 'IN_PROGRESS'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'New Task')


class UpdateTaskViewTests(TestCase):
    def test_update_task(self):
        task = Task.objects.create(title="Task 1", description="Task 1 description",
                                   due_date="2024-09-10", priority=1, status="IN_PROGRESS")
        response = self.client.post(reverse('update-task', args=[task.id]), {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'due_date': '2024-09-15',
            'priority': 1,
            'status': 'IN_PROGRESS'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task-list'))
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'Updated Task')


class DeleteTaskViewTests(TestCase):
    def test_delete_task(self):
        task = Task.objects.create(title="Task 1", description="Task 1 description",
                                   due_date="2024-09-10", priority=1, status="To Do")
        response = self.client.post(reverse('delete-task', args=[task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task-list'))
        self.assertEqual(Task.objects.count(), 0)
