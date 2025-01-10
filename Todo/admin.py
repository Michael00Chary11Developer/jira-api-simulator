from django.contrib import admin
from .models import WorkLog, Task

# Register your models here.

admin.site.register(WorkLog)
admin.site.register(Task)