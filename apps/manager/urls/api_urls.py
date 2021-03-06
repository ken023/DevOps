from django.conf.urls import url
from ..api import group as GroupAPI
from ..api import systype as SystypeAPI
from ..api import position as PositionAPI
from ..api import host as HostAPI
# from .. import api
urlpatterns=[
    # Resource group api
    url(r'^v1/group/$', GroupAPI.ManagerGroupListAPI.as_view()),
    url(r'^v1/group/create/$', GroupAPI.ManagerGroupCreateAPI.as_view()),
    url(r'^v1/group/(?P<pk>[0-9]+)/detail/$', GroupAPI.ManagerGroupDetailAPI.as_view()),
    url(r'^v1/group/(?P<pk>[0-9]+)/update/$',GroupAPI.ManagerGroupUpdateAPI.as_view()),
    url(r'^v1/group/(?P<pk>[0-9]+)/delete/$',GroupAPI.ManagerGroupDeleteAPI.as_view()),
    #
    # Resource systype api
    url(r'^v1/systype/$', SystypeAPI.ManagerSystypeListAPI.as_view()),
    url(r'^v1/systype/create/$', SystypeAPI.ManagerSystemCreateAPI.as_view()),
    url(r'^v1/systype/(?P<pk>[0-9]+)/detail/$', SystypeAPI.ManagerSystemDetailAPI.as_view()),
    url(r'^v1/systype/(?P<pk>[0-9]+)/update/$', SystypeAPI.ManagerSystemUpdateAPI.as_view()),
    url(r'^v1/systype/(?P<pk>[0-9]+)/delete/$', SystypeAPI.ManagerSystemDeleteAPI.as_view()),
    #
    # Resource position api
    url(r'^v1/position/$', PositionAPI.ManagerPositionListAPI.as_view()),
    url(r'^v1/position/create/$', PositionAPI.ManagerPositionCreateAPI.as_view()),
    url(r'^v1/position/(?P<pk>[0-9]+)/detail/$', PositionAPI.ManagerPositionDetailAPI.as_view()),
    url(r'^v1/position/(?P<pk>[0-9]+)/update/$', PositionAPI.ManagerPositionUpdateAPI.as_view()),
    url(r'^v1/position/(?P<pk>[0-9]+)/delete/$', PositionAPI.ManagerPositionDeleteAPI.as_view()),
    #
    # Resource host api
    url(r'^v1/hostbygroup/(?P<pk>[0-9]+)/$',HostAPI.ManagerHostListByGroupAPI.as_view()),
    url(r'^v1/host/$',HostAPI.ManagerHostListAPI.as_view()),
    url(r'^v1/host/create/$', HostAPI.ManagerHostCreateAPI.as_view()),
    url(r'^v1/host/(?P<pk>[0-9]+)/detail/$', HostAPI.ManagerHostDetailAPI.as_view()),
    url(r'^v1/host/(?P<pk>[0-9]+)/update/$', HostAPI.ManagerHostUpdateAPI.as_view()),
    url(r'^v1/host/(?P<pk>[0-9]+)/delete/$', HostAPI.ManagerHostDeleteAPI.as_view()),
    url(r'^v1/host/(?P<pk>[0-9]+)/passwd/$', HostAPI.ManagerHostPasswordAPI.as_view()),
    #
    # # Resource storage api
    # url(r'^v1/storage/$', api.ManagerStorageListAPI.as_view()),
    # url(r'^v1/storage/(?P<pk>[0-9]+)/remove/', api.ManagerStorageRemoveAPI.as_view()),
    #
    # # Resource search api
    # url(r'^v1/search/',api.ManagerSearchAPI.as_view()),
]