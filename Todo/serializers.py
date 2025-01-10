from rest_framework import serializers
from .models import work_log, Task


class WorkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = work_log
        fields = ['task', 'description', 'date','Time_spent']


class TaskSerialier(serializers.ModelSerializer):
    work_log_Test = WorkLogSerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = '__all__'
        #fields = ['task', 'description', 'time_spent', 'date'] 
        # fields = ['id', 'Title', 'status', 'user','work]
        


