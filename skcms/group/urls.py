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

urlpatterns = [
    url(r'^group$', views.GroupView.as_view(), name="group"),

    # url(r'^address_book/person/(?P<pk>(\d)+)$', views.PersonView.as_view(), name="person"),
    # url(r'^address_book/person_edit/(?P<pk>(\d)+)$', views.PersonEditView.as_view(), name="person_edit"),
    # url(r'^address_book/person_del/(?P<pk>(\d)+)$', views.PersonDelView.as_view(), name="person_del"),
    # url(r'^address_book/person_new', views.PersonNewView.as_view(), name="person_new"),
]

urlpatterns += staticfiles_urlpatterns()
