from django.test import TestCase
from .models import Task


class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="Sample Task", completed=False)
        self.assertEqual(task.title, "Sample Task")
        self.assertFalse(task.completed)

    def test_mark_task_completed(self):
        task = Task.objects.create(title="Test Complete Task", completed=False)
        task.completed = True
        task.save()
        self.assertTrue(Task.objects.get(pk=task.pk).completed)