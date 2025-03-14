from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    create_task,
    mark_task_completed
)

app_name = "task_manager_api"

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', create_task, name='task_create'),
    path('tasks/<int:pk>/complete/', mark_task_completed, name='task_complete')
]
