from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from .forms import GroupForm, GroupPersonForm
from .models import Group, GroupPerson, Person


class GroupsView(TemplateView):
    def get(self, request):
        groups = Group.objects.all().order_by('name')
        return render(request=request, template_name="group/groups.html",
                      context={'groups': groups})


class GroupNewView(TemplateView):
    def get(self, request):
        group = GroupForm()
        ctx = {"form_group": group, "title": "Group"}
        return TemplateResponse(request, 'group/group_new.html', ctx)

    def post(self, request):
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group = group_form.save(commit=True)
            return HttpResponseRedirect(reverse('group:group_detail', args=(group.id,)))


class GroupEditView(TemplateView):

    def get(self, request, id):
        if id:
            instance_group = get_object_or_404(Group, id=id)

            group_form = GroupForm(request.POST or None, instance=instance_group)

            ctx = {"group_form": group_form,
                   "title": "Person", "id": id}

            return TemplateResponse(request, 'group/group_edit.html', ctx)

    def post(self, request, id):
        instance_group = get_object_or_404(Group, id=id)
        group_form = GroupForm(request.POST or None, instance=instance_group)

        if group_form.is_valid():
            person = group_form.save(commit=False)
            person.save()
            return HttpResponseRedirect(reverse('group:group_edit', args=(id,)))



class GroupPersonAddView(TemplateView):
    def get(self, request, pk):
        group_person_form = GroupPersonForm()
        ctx = {"group_person_form": group_person_form, "title": "Add Person to group " + str(pk)}
        return TemplateResponse(request, 'group/group_person.html', ctx)

    def post(self, request, pk):
        group_person_form = GroupPersonForm(request.POST)
        if group_person_form.is_valid():
            group_person = group_person_form.save(commit=False)
            group_person.group_id = int(pk)
            group_person.save()
            return HttpResponseRedirect(reverse('group:group_person', args=(pk,)))


class GroupDetailView(generic.DetailView):

    def get(self, request, pk):
        group_detail_form = get_object_or_404(Group, id=pk)

        # import ipdb
        # ipdb.set_trace()

        return render(request=request, template_name="group/group_detail.html",
                      context={'group_detail_form': group_detail_form})


class GroupDelView(generic.DetailView):

    def get(self, request, pk):
        try:
            group = get_object_or_404(Group, id=pk)
            group.delete()
        except:
            pass

        return HttpResponseRedirect(reverse('group:groups'))


class GroupPersonDelView(TemplateView):

    def get(self, request, group_id, person_id):
        related = GroupPerson.objects.filter(group_id=group_id, person_id=person_id)
        related.delete()
        return HttpResponseRedirect('group:group_detail', args=(group_id,))
