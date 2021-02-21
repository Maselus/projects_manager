from django.urls import path

from projects_and_tasks.views import HomeView, ProjectListView, ProjectDetailView, TaskListView, \
    TaskDetailView, ProjectCreateView, TaskCreateView, ProjectDeleteView, TaskDeleteView, \
    ProjectUpdateView, TaskUpdateView, CalendarView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # project urls
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),

    # task urls
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),

    # calendar
    path('calendar/', CalendarView.as_view(), name='calendar'),
]
