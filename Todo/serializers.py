from rest_framework import serializers
from .models import work_log, Task


class WorkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = work_log
        # fields = ['task', 'description', 'date', 'Time_spent', 'id']
        fields = ['description', 'Time_spent', 'task', 'status']

        # extra_kwargs = {"date": {"required": False}}



class TaskSerializer(serializers.ModelSerializer):
    # work_log_Test = WorkLogSerializer(read_only=True, many=True)

    class Meta:
        model = Task

        # fields = ['ticket_id', 'Title', 'work_log_Test', 'user']
        fields = '__all__'
        # fields = ['task', 'description', 'time_spent', 'date']
        # fields = ['id', 'Title', 'status', 'user','work]
