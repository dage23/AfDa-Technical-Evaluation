from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from tasks.models import Task
from tasks.serializer import TaskSerializer# Create your views here.

class TasksView(APIView):
    def get(self,request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)