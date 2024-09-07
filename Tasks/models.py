from django.db import models


class Task(models.Model):

    # Choices for priority
    class Priority(models.IntegerChoices):
        HIGH = 1
        MEDIUM = 2
        LOW = 3

    # Choices for status
    class Status(models.TextChoices):
        TODO = 'TODO', 'To Do'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        DONE = 'DONE', 'Done'

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.IntegerField(
        choices=Priority.choices, default=Priority.MEDIUM)
    status = models.CharField(
        max_length=max(len(value) for value, label in Status.choices),
        choices=Status.choices, default=Status.TODO)
