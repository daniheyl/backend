from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    # def ready(self):
    #     from .models import Status
    #     if not Status.objects.exists():
    #         Status.objects.bulk_create([
    #             Status(name='Pending', description='Task is pending'),
    #             Status(name='In Progress', description='Task is being worked on'),
    #             Status(name='Completed', description='Task is finished'),
    #         ])
