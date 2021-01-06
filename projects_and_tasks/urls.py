from django.urls import path

from projects_and_tasks.views import HomeView, ProjectListView, ProjectDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]
