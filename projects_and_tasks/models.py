from django.db import models
from django_enumfield import enum

from projects_and_tasks.enums import TaskStatus


class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=16)
    task_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='tasks')
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    number = models.IntegerField()
    deadline = models.DateField(null=True, blank=True)
    status = enum.EnumField(TaskStatus)

    def __str__(self):
        return f"{self.project.code}-{self.number}"


class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    projects = models.ManyToManyField(Project, related_name='users')
