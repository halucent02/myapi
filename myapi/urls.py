"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='My API')

admin.site.site_header    = 'myapi admin'
admin.site.site_title     = 'myapi admin'
admin.site.site_url       = '/'
admin.site.index_title    = 'myapi administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^swagger/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^item/', include('item.urls',namespace="item")),
    url(r'^set/', include('set.urls',namespace="set")),
    url(r'^group/', include('group.urls',namespace="group")),
]
