from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from projects_and_tasks.models import Project, Task


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Project'))


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'project', 'deadline', 'status', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Task'))

