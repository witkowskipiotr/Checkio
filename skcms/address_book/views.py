from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.views import View

from .models import Address, Person
from .forms import Address as AddresForm, NameForm
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.forms import ModelForm


class MyFormView(View):

    def get(self, request):
        address = Address.objects.get(pk=1)
        # form = AddresForm(instance=address)

        form = NameForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = NameForm()
        if form.is_valid():
            login = form.cleaned_data['login']
            return HttpResponseRedirect('/thanks/')
        a = form.is_valid()
        print(a)

class AddressView(TemplateView):

    def get(self, request):
        persons = Address.objects.all()
        persons = {}
        # return render(request=request, template_name="persons.html", context=persons)
        return TemplateResponse(request=request, template="address_list.html", context=persons)

    def post(self, requerst):
        print(1)
        return


class PersonView(TemplateView):

    def get(self, request):
        persons = {
            "name": "Łukasz",
            "surname": "Witkowski"
        }

        # return render(request=request, template_name="persons.html", context=persons)
        return render(request=request, template_name="base.html", context=persons)

    def post(self, requerst):
        print(1)
        return


class NewPersonView(TemplateView):
    def post(self, request):
        addres = Address.objects.create(city="Płock", street="Mickiewicza",
                                        number_house=2, number_flat=2)
        print(2)

    def get(self, request):
        form = AddresForm
        print(form)
        return render_to_response('new_person_2.html', {'form': AddresForm})