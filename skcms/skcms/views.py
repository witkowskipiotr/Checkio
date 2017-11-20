from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


# from .forms import AddressForm, PersonForm, PhoneForm, EmailForm
# from .models import Address, Person, Email, Phone


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
    ctx = {'user_name': request.user.username}
    return render(request=request, template_name="loggedin.html", context=ctx)


def log_out_view(request):
    auth.logout(request)
    return render(request=request, template_name="logout.html")


def invalid_login_view(request):
    return render(request=request, template_name="invalid_login.html")


def create_user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/accounts/create_user_success')

    ctx = {'forms': UserCreationForm()}
    return render(request=request, template_name="create_user.html", context=ctx)


def create_user_success_view(request):
    return render(request=request, template_name='create_user_success.html')
