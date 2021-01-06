from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView

from projects_and_tasks.models import Project


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'project_list.html'

    def get_queryset(self):
        return Project.objects.filter(users_profiles__user=self.request.user).all()


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project_detail.html'