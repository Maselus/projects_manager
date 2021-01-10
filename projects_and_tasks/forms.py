from django.forms import ModelForm, ModelMultipleChoiceField

from projects_and_tasks.models import Project, UserProfile


class ProjectCreateForm(ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'code']

