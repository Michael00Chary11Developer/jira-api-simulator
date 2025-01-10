from django.urls import path, include
from .views import ListViewApiView, DetailViewApiView, ListMixinApi

urlpatterns = [
    # path("get_all/", ListViewApiView.as_view(), name='get_all'),
    # path("post/",ListViewApiView.as_view(),name='post'),
    path("ListView/", ListViewApiView.as_view(), name="ListView"),
    path("DetailListView/<int:task_id>/",
         DetailViewApiView.as_view(), name="DetailListView"),
    path("MixinListView/", ListMixinApi.as_view(), name='MixinListView'),
]