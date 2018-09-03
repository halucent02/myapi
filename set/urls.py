from django.conf.urls import url
from .views import SetListCreateView, SetRetrieveView
urlpatterns = [
    url(r'^$', SetListCreateView.as_view()),
    url(r'^(?P<pk>\d+)/$', SetRetrieveView.as_view()),
]
