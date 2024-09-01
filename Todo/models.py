from django.db import models
from django.contrib.auth.models import User
# from rest_framework import viewsets


class Task(models.Model):

    # status_choice = [('Not started'), ('Done'), ("InProgeress")]

    id = models.AutoField(primary_key=True)
    ticket_id = models.IntegerField(blank=False)
    Title = models.CharField(max_length=250, blank=False)
    # status = models.CharField(
    #     max_length=20, default="Not started")
    user = models.ForeignKey(User, related_name='Task',
                             on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.ticket_id},{self.Title}'


class work_log(models.Model):
    task = models.ForeignKey(
        Task, related_name="work_log_Test", on_delete=models.CASCADE)
    description = models.TextField()
    Time_spent = models.CharField(max_length=10, blank=False)
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
