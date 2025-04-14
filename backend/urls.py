from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks import views


router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'statuses', views.StatusViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/', include(router.urls)),
]
