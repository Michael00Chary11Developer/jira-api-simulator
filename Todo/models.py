from django.db import models
from django.contrib.auth.models import User
# from rest_framework import viewsets


class Task(models.Model):

    id = models.AutoField(primary_key=True)
    ticket_id = models.IntegerField(blank=False)
    title = models.CharField(max_length=250, blank=False)
    # status = models.CharField(
    #     max_length=20, default="Not started")
    user = models.ForeignKey(User, related_name='Task',
                             on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.ticket_id},{self.title}'


class WorkLog(models.Model):
    task = models.ForeignKey(
        Task, related_name="work_log_test", on_delete=models.CASCADE)
    description = models.TextField()
    time_spent = models.CharField(max_length=10, blank=False)
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
