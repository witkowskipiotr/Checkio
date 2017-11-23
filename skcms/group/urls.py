"""skcms URL Configuration

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
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


app_name = 'group'

urlpatterns = [
    url(r'^group/$', views.GroupsView.as_view(), name="groups"),
    url(r'^group/group_new$', views.GroupNewView.as_view(), name="group_new"),
    # ex: /group/group_detail/4
    url(r'^group/group_detail/(?P<pk>[0-9]+)$', views.GroupDetailView.as_view(), name='detail'),
    url(r'^group/group_person_add/(?P<pk>[0-9]+)$', views.GroupPersonAddView.as_view(), name='group_person'),
]

urlpatterns += staticfiles_urlpatterns()
