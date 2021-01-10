from django.contrib import admin

from projects_and_tasks.models import Project, Task, UserProfile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fieldsets = (None, {
        'fields': ('project', 'name', 'description', 'deadline')
    }),


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = (None, {
        'fields': ('user', )
    }),
    inlines = [
        ProjectInline,
    ]
