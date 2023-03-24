from django.urls import path
from .views import TasksView

app_name = "tasks"

urlpatterns = [
    path('tasks/', TasksView.as_view()),
]