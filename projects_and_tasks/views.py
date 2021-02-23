import calendar
from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, \
    UpdateView
from django_filters.views import FilterView

from projects_and_tasks.calendar import Calendar
from projects_and_tasks.filters import TaskFilter
from projects_and_tasks.forms import ProjectForm, TaskForm
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

    def get_queryset(self):
        return Project.objects.filter(owner__user=self.request.user).all()


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_create.html'

    def get_success_url(self):
        return reverse('project_list')

    def form_valid(self, form):
        form.instance.owner_id = UserProfile.objects.get(user_id=self.request.user.id).id
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/project_update.html'

    def get_success_url(self):
        return reverse_lazy('project_detail', args=[self.object.id])

    def get_queryset(self):
        return Project.objects.filter(owner__user=self.request.user).all()


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')

    def get_queryset(self):
        return Project.objects.filter(owner__user=self.request.user).all()


# Task views
class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'task/task_list.html'
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.filter(project__owner__user=self.request.user).all()


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task_detail.html'

    def get_queryset(self):
        return Task.objects.filter(project__owner__user=self.request.user).all()


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_create.html'

    def get_success_url(self):
        return reverse('task_list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TaskForm
    model = Task
    template_name = 'task/task_update.html'

    def get_success_url(self):
        return reverse_lazy('task_detail', args=[self.object.id])

    def get_queryset(self):
        return Task.objects.filter(project__owner__user=self.request.user).all()


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(project__owner__user=self.request.user).all()


# Calendar View
class CalendarView(LoginRequiredMixin, ListView):
    template_name = 'deadlines_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cal = Calendar(
            user=self.request.user,
            year=context['view'].kwargs['year'],
            month=context['view'].kwargs['month']
        )

        html_cal = cal.format_month(with_year=True)
        context['calendar'] = mark_safe(html_cal)
        this_date = datetime(year=context['view'].kwargs['year'], month=context['view'].kwargs['month'], day=1)
        next_date = (this_date + timedelta(days=32)).replace(day=1)
        prev_date = (this_date - timedelta(days=1)).replace(day=1)
        context['next_year'] = next_date.year
        context['prev_year'] = prev_date.year
        context['next_month'] = next_date.month
        context['prev_month'] = prev_date.month

        return context

    def get_queryset(self):
        return Task.objects.filter(project__owner__user=self.request.user).all()
