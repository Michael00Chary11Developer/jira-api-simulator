from rest_framework import serializers
from .models import WorkLog, Task


class WorkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkLog
        # fields = ['task', 'description', 'date', 'Time_spent', 'id']
        # fields = ['description', 'time_spent', 'task', 'status']
        fields = '__all__'

        # extra_kwargs = {"date": {"required": False}}


class TaskSerializer(serializers.ModelSerializer):
    work_log_test = WorkLogSerializer(read_only=True, many=True)  # for get
    # work_log_test = WorkLogSerializer(many=True, write_only=True)  #for post

    class Meta:
        model = Task

        # fields = ['ticket_id', 'Title', 'work_log_test', 'user']
        fields = '__all__'
        # fields = ['task', 'description', 'time_spent', 'date']
        # fields = ['id', 'Title', 'status', 'user','work]
        # fields = ["ticket_id", "title", "work_log_test", "user"]
