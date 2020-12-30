from django.test import TestCase

from projects_and_tasks.models import Project, Task


class TaskModelTest(TestCase):

    def test_task_create_increment_project_task_counter(self):
        project = Project.objects.create(
            name='test',
            code='ABC'
        )
        self.assertEqual(project.task_counter, 0)
        task = Task.objects.create(
            project=project,
            name="test_task",
        )
        self.assertEqual(task.number, 0)
        project.refresh_from_db()
        self.assertEqual(project.task_counter, 1)

