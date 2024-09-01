import logging
import traceback
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer, WorkLogSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import mixins, generics

class ListViewApiView(APIView):

    def get(self, requset: Request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        try:
            data = request.data
            serializer = WorkLogSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
            else:
                logging.error(traceback.format_exc())
                return Response(None, status.HTTP_400_BAD_REQUEST)
        except:
            logging.error(traceback.format_exc())
            return Response(None, status.HTTP_400_BAD_REQUEST)


class DetailViewApiView(APIView):
    # DetailViewApiView.get_object_by_id() missing 1 required positional argument: 'request'
    # def get_object_by_id(self, request: Request, task_id: int):
    #     task = Task.objects.filter(pk=task_id)
    #     try:
    #         task = Task.objects.get(pk=task_id)
    #         return task
    #     except Task.DoesNotExist:
    #         return Response(None, status.HTTP_204_NO_CONTENT)
    def get_object_by_id(self, task_id: int):
        task = Task.objects.filter(pk=task_id)
        try:
            task = Task.objects.get(pk=task_id)
            return task
        except Task.DoesNotExist:
            return Response(None, status.HTTP_204_NO_CONTENT)

    def get(self, request: Request, task_id: int):
        task = self.get_object_by_id(task_id=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, task_id: int):
        task = self.get_object_by_id(task_id=task_id)
        serializer = TaskSerializer(task, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, task_id: int):
        task = self.get_object_by_id(task_id=task_id)
        if task is not None:
            task.delete()
            return Response(None, status.HTTP_508_LOOP_DETECTED)
        return Response(None, status.HTTP_204_NO_CONTENT)


# region mixins
class ListMixinApi(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)