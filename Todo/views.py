import logging
import traceback
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task, WorkLog
from .serializers import TaskSerializer, WorkLogSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import mixins, generics


class ListViewApiView(APIView):

    def get(self, requset: Request):
        try:
            task = Task.objects.all()
            serializer = TaskSerializer(task, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as ex:
            logging.error(traceback.format_exc)
            return Response({'detail': str(ex)}, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request: Request):
        try:
            data = request.data
            serializer = TaskSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
            else:
                logging.error("Validation error: %s", serializer.errors)
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logging.error(traceback.format_exc())
            return Response({'detail': str(ex)}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetTaskByObjectById:
    def get_task_by_id(self, task_id: int):
        try:
            task = Task.objects.get(pk=task_id)
            return task
        except Task.DoesNotExist:
            return Response(None, status.HTTP_204_NO_CONTENT)


class DetailViewApiView(APIView, GetTaskByObjectById):

    def get(self, request: Request, task_id: int):
        try:
            task = self.get_task_by_id(task_id=task_id)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            status.HTTP_204_NO_CONTENT

    def put(self, request: Request, task_id: int):
        task = self.get_task_by_id(task_id=task_id)
        serializer = TaskSerializer(task, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, task_id: int):
        task = self.get_task_by_id(task_id=task_id)
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


class ApiViewAddWorkLog(APIView, GetTaskByObjectById):
    def get(self, request: Request, task_id: int):
        task = self.get_task_by_id(task_id=task_id)
        serilazer = TaskSerializer(task)
        return Response(serilazer.data, status.HTTP_202_ACCEPTED)

    def post(self, request: Request, task_id: int):
        task = self.get_task_by_id(task_id)
        if not task:
            return Response({'detail': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data["task"] = task_id
        serializer = WorkLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logging.error("Validation error: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailApiViewAddWorkLog(APIView, GetTaskByObjectById):
    def get(self, request: Request, task_id: int, work_log_id: int):
        # task = Task.objects.get(pk=task_id)
        task = self.get_task_by_id(task_id=task_id)
        if not task:
            logging.error("Not found Task!")
            return Response(None, status.HTTP_400_BAD_REQUEST)
        work_log = WorkLog.objects.get(pk=work_log_id)
        serializer = WorkLogSerializer(work_log)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, task_id: int, work_log_id: int):
        task = self.get_task_by_id(task_id)
        if not task:
            return Response({'detail': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            work_log = WorkLog.objects.get(pk=work_log_id)
        except WorkLog.DoesNotExist:
            return Response({'detail': 'WorkLog not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WorkLogSerializer(
            work_log, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, task_id: int, work_log_id: int):
        task = self.get_task_by_id(task_id)
        if not task:
            return Response({'detail': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            work_log = WorkLog.objects.get(pk=work_log_id)
            work_log.delete()
            return Response({'detail': 'WorkLog deleted'}, status=status.HTTP_204_NO_CONTENT)
        except WorkLog.DoesNotExist:
            return Response({'detail': 'WorkLog not found'}, status=status.HTTP_404_NOT_FOUND)

