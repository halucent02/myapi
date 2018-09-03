from django.conf.urls import url
from .views import ItemListCreateView, ItemRetrieveView
urlpatterns = [
    url(r'^$', ItemListCreateView.as_view()),
    url(r'^(?P<pk>\d+)/$', ItemRetrieveView.as_view()),
]
