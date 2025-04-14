from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Task, Status
from .serializers import TaskSerializer, StatusSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all().order_by('order')
    serializer_class = StatusSerializer
    # Add this to require authentication
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    # Add this to require authentication
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return tasks belonging to the logged-in user
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically set the user field to the current user when creating a task
        serializer.save(user=self.request.user)
