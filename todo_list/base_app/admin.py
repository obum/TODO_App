from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_filter = ('user','title', 'complete', 'created_at')
    search_fields = ('title', 'complete', 'created_at')

admin.site.register(Task, TaskAdmin)