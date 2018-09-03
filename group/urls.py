from django.conf.urls import url
from .views import GroupListCreateView, GroupRetrieveView
urlpatterns = [
    url(r'^$', GroupListCreateView.as_view()),
    url(r'^(?P<pk>\d+)/$', GroupRetrieveView.as_view()),
]
