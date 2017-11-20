from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from .forms import GroupForm, GroupPersonForm
from address_book.models import Group, GroupPerson, Person


class GroupView(TemplateView):
    def get(self, request):
        groups = Group.objects.all().order_by('name')
        return render(request=request, template_name="groups.html",
                      context={'groups': groups})