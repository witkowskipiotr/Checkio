from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.serializers import json
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from notifications.models import Notifications, User
from django.contrib.auth import get_user_model


# from .forms import AddressForm, PersonForm, PhoneForm, EmailForm
# from .models import Address, Person, Email, Phone

# change model in creation form
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {'username': UsernameField}


def login_view(request):
    return TemplateResponse(request=request, template="login.html")
    # return render(request=request, template_name="login.html")


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user:
        auth.login(request=request, user=user)
        return redirect(to='/accounts/loggedin/')
    return redirect(to='/accounts/invalid/')


def logged_in_view(request):
    notification = Notifications.objects.filter(user=request.user, viewed=False)
    ctx = {
        'user_name': request.user.username,
        'notifications': notification
    }
    return render(request=request, template_name="loggedin.html", context=ctx)


def log_out_view(request):
    auth.logout(request)
    return render(request=request, template_name="logout.html")


def invalid_login_view(request):
    return render(request=request, template_name="invalid_login.html")


def create_user_view(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/accounts/create_user_success')

    ctx = {'forms': MyUserCreationForm(), 'title': 'Create User'}

    # return render(request=request, template_name="create_user.html",
    #               context=ctx)
    from django.http import HttpResponse
    # return HttpResponse(
    #     ctx=json.dumps(ctx),
    #     content_type="application/json",
    #     template_name="create_user.html"
    # )


    return render(request=request, template_name="create_user.html",
                  context=ctx)


def create_user_success_view(request):
    ctx = {'title': 'User create success'}
    return render(request=request, template_name='base.html', context=ctx)
