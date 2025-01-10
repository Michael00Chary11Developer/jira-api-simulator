from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register('', TaskViewSet)


urlpatterns = [
    path("get/", views.GetTask.as_view(), name='get'),
    path("all_task", views.all_task, name="get2"),
    path("all_work/", views.all_work_log),
    path('viewsets/', include(router.urls)),
    path("all_work_log/", views.all_work_log, name="work"),
    # path("get/",views.GetTaskViewSet.as_view(),name='viewsets')
    # path("viewsets/", include(router.urls))
    # path("post/", , name='post')
]
