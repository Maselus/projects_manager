import django_filters

from projects_and_tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['project', 'status']
