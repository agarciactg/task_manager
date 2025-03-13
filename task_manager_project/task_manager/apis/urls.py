from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    create_task,
    mark_task_completed
)

app_name = "task_manager_api"

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/create/', create_task, name='task-create'),
    path('tasks/<int:pk>/complete/', mark_task_completed, name='task-complete')
]
