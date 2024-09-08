from django.test import TestCase
from .models import Task
import datetime


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
