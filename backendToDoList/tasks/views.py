from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets

from tasks.models import Task
from tasks.serializer import TaskSerializer# Create your views here.

class TasksView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset  = Task.objects.all()