from django.db import models
from django.db.transaction import atomic
from django_enumfield import enum

from projects_and_tasks.enums import TaskStatus


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.PROTECT)


class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=16)
    task_counter = models.IntegerField(default=0)
    owner = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name='projects')

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    number = models.IntegerField(auto_created=True)
    deadline = models.DateField(null=True, blank=True)
    status = enum.EnumField(TaskStatus, default=0)

    def __str__(self):
        return f"{self.project.code}-{self.number}"

    @atomic
    def save(self, *args, **kwargs):
        if not self.id:
            project = Project.objects.select_for_update().filter(id=self.project_id).get()
            self.number = project.task_counter
            project.task_counter += 1
            project.save()
        super().save(*args, **kwargs)

