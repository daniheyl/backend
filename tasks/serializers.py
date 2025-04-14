from rest_framework import serializers
from .models import Task, Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description',
                  'status']  # Must match Angular form
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True},
            'status': {'required': True}
        }
