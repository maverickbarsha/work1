from django.conf.urls import url

from .views import (
    TCreate,
    TList,
    TUpdate,
    TDelete,
    )

urlpatterns = [
    url(r'^$', TList.as_view(), name='t_list'),
    url(r'^create/$', TCreate.as_view(), name='t_create'),
    url(r'^(?P<pk>\d+)/edit/$', TUpdate.as_view(), name='t_edit'),
    url(r'^(?P<pk>\d+)/delete/$', TDelete.as_view(), name='t_delete'),
    ]