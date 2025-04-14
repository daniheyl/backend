from django.contrib import admin
from tasks.models import Status, Task

# Register your models here.


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'created_at')
    list_filter = ('status', 'user')
