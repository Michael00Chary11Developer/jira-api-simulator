from django.shortcuts import render
from .models import Task, work_log
from rest_framework import generics, viewsets
from .serializers import WorkLogSerializer, TaskSerialier
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

# generics


class GetTask(generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialier


# viewset
class GetTaskViewSet(viewsets.ViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialier


@api_view(['GET', 'POST'])
def all_task(request: Request):
    if request.method == 'GET':
        todos = Task.objects.all()
        todo_serializer = TaskSerialier(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serailizer = TaskSerialier(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data, status.HTTP_201_CREATED)
    return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def all_work_log(request: Request):
    if request.method == 'GET':
        todos = work_log.objects.all()
        todo_serializer = WorkLogSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serailizer = WorkLogSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data, status.HTTP_201_CREATED)
    return Response(None, status.HTTP_400_BAD_REQUEST)


     
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialier