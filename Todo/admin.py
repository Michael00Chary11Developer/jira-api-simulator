from django.contrib import admin
from .models import work_log, Task

# Register your models here.

admin.site.register(work_log)
admin.site.register(Task)