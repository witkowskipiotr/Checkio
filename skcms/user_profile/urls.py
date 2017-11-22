from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.user_profile, name="profile"),
    # url(r'^address_book$', views.user_profile, name="persons"),
]

