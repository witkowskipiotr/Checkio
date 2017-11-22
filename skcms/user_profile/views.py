from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(to="/accounts/loggedin/")

    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)
        ctx = {'forms': form}
        return render(request=request, template_name="user_profile.html",
                      context=ctx)