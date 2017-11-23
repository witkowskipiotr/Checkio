from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from .models import Notifications


def index(request):
    notification = Notifications.objects.filter(user=request.user)
    ctx = {'notifications': notification}
    return render(request=request, template_name="index.html",
                  context=ctx)

def show_notification(request, notification_id):
    notification = Notifications.objects.get(id=notification_id)
    ctx = {'notification': notification}
    return render(request=request, template_name="notification.html",
                  context=ctx)


def delete_notification(request, notification_id):
    notification = Notifications.objects.get(id=notification_id)
    notification.viewed = True
    notification.save()
    return redirect(to='/accounts/loggedin')
