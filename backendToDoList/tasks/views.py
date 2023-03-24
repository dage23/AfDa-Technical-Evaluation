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
    
    def post(self, request):
        data = {
                    'title': request.data.get('title'), 
                    'completed': request.data.get('completed'), 
                }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)