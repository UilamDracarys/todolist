from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_on', 'updated_on')
    list_display_links = ('title',)


admin.site.register(Task, TaskAdmin)
