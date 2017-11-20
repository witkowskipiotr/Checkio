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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'', include('address_book.urls')),
    url(r'', include('group.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login_view, name='login'),
    url(r'^accounts/auth/$', views.auth_view, name='auth'),
    url(r'^accounts/logout/$', views.log_out_view, name='logout'),
    url(r'^accounts/loggedin/$', views.logged_in_view, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login_view, name='invalid'),

    url(r'^accounts/create_user/$', views.create_user_view, name='create_user'),
    url(r'^accounts/create_user_success/$', views.create_user_success_view, name='create_user_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
