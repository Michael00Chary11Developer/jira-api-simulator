from django.urls import path, include
from .views import ListViewApiView, DetailViewApiView, ListMixinApi, DetailApiViewAddWorkLog, ApiViewAddWorkLog

urlpatterns = [

    path("ListView/", ListViewApiView.as_view(), name="ListView"),
    path("ListView/<int:task_id>/",
         DetailViewApiView.as_view(), name="DetailListView"),
    path("MixinListView/", ListMixinApi.as_view(), name='MixinListView'),
    path("WorkLog/task/<int:task_id>/",
         ApiViewAddWorkLog.as_view(), name='AddWorkLog'),
    path("WorkLog/task/<int:task_id>/work_log/<int:work_log_id>/",
         DetailApiViewAddWorkLog.as_view(), name='EditAndDeleteWorkLog'),
]
