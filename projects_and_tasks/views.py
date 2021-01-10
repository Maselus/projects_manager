from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, \
    UpdateView

from projects_and_tasks.forms import ProjectCreateForm
from projects_and_tasks.models import Project, Task, UserProfile


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


# Project views
class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'project/project_list.html'

    def get_queryset(self):
        return Project.objects.filter(owner__user=self.request.user).all()


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project/project_detail.html'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'project/project_create.html'

    def get_success_url(self):
        return reverse('project_list')

    def form_valid(self, form):
        form.instance.owner_id = UserProfile.objects.get(user_id=self.request.user.id).id
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'code']
    template_name = 'project/project_update.html'

    def get_success_url(self):
        return reverse_lazy('project_detail', args=[self.object.id])


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')


# Task views
class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'task/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(project__owner__user=self.request.user).all()


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'project', 'deadline']
    template_name = 'task/task_create.html'

    def get_success_url(self):
        return reverse('task_list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'deadline', 'status']
    template_name = 'task/task_update.html'

    def get_success_url(self):
        return reverse_lazy('task_detail', args=[self.object.id])


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

