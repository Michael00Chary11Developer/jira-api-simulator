from django.urls import path, include
from .views import ListViewApiView, DetailViewApiView, ListMixinApi, DetailApiViewAddWorkLog, ApiViewAddWorkLog

urlpatterns = [
    # path("get_all/", ListViewApiView.as_view(), name='get_all'),
    # path("post/",ListViewApiView.as_view(),name='post'),
    path("ListView/", ListViewApiView.as_view(), name="ListView"),
    path("ListView/<int:task_id>/",
         DetailViewApiView.as_view(), name="DetailListView"),
    path("MixinListView/", ListMixinApi.as_view(), name='MixinListView'),
    # # # # path("WorkLog/task/<int:task_id>",
    # # # #      DetailApiViewAddWorkLog.as_view(), name='GetAndPost'),
    # # # # path("WorkLog/task/<int:task_id>/work_log/<int:work_log_id>",
    # # # #      DetailApiViewAddWorkLog.as_view(), name='PutAndDelete'),
    # path("WorkLog/task/<int:task_id>/work_log/<int:work_log_id>/",
    #      DetailApiViewAddWorkLog.as_view(), name='PutAndDelete')
    path("WorkLog/task/<int:task_id>/",
         ApiViewAddWorkLog.as_view(), name='AddWorkLog'),
    path("WorkLog/task/<int:task_id>/work_log/<int:work_log_id>/",
         DetailApiViewAddWorkLog.as_view(), name='EditAndDeleteWorkLog'),
]
