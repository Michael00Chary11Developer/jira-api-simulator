from rest_framework import serializers
from .models import WorkLog, Task


class WorkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkLog
        fields = '__all__'




class TaskSerializer(serializers.ModelSerializer):
    work_log_test = WorkLogSerializer(read_only=True, many=True)
 
    class Meta:
        model = Task

        fields = '__all__'
