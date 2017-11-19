from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from .forms import AddressForm, PersonForm, PhoneForm, EmailForm
from .models import Address, Person, Email, Phone


class AddressView(TemplateView):
    def get(self, request, pk):
        data = {}
        if pk:
            detail = Address.objects.get(pk=pk)
            if detail:
                data['city'] = detail.city
                data['street'] = detail.street
                data['number_flat'] = detail.number_flat
                data['number_house'] = detail.number_house
        return TemplateResponse(request, 'address_detail.html', data)

    def post(self, request):
        id = request.POST.get("id")
        if id:
            instance = get_object_or_404(Address, id=1)
            form = AddressForm(request.POST or None, instance=instance)
            data = {"forms": form, "title": "addres"}
            return TemplateResponse(request, 'address_new.html', data)

        return TemplateResponse(request, 'address_detail.html', request)


class AddressNewView(TemplateView):
    def get(self, request):
        form = AddressForm()
        data = {"forms": form, "title": "address"}
        return TemplateResponse(request, 'address_new.html', data)

    def post(self, request):
        form = AddressForm(request.POST)
        data = {}
        if form.is_valid():
            address = form.save(commit=False)
            # address.author = request.user
            # address.published_date = timezone.now()
            address.save()
            return redirect('address_detail', pk=address.pk)


class PersonsView(TemplateView):
    def get(self, request):
        persons = Person.objects.all()
        return render(request=request, template_name="persons.html",
                      context={'persons': persons})


class PersonView(TemplateView):
    
    def get(self, request, pk):
        ctx = {}
        if pk:
            person = Person.objects.get(pk=pk)
            address = Address.objects.get(pk=person.address_id)
            phone = Phone.objects.get(pk=person.phone_id)
            email = Email.objects.get(pk=person.email_id)
            if person:
                ctx['name'] = person.name
                ctx['surname'] = person.surname
                ctx['description'] = person.description

                ctx['city'] = address.city
                ctx['street'] = address.street
                ctx['number_flat'] = address.number_flat
                ctx['number_house'] = address.number_house

                ctx['number_phone'] = phone.number_phone
                for type_email in email.TYPE_EMAIL:
                    if type_email[0] == email.type:
                        ctx['type_phone'] = type_email[1]

                ctx['email'] = email.email
                for type_email in email.TYPE_EMAIL:
                    if type_email[0] == email.type:
                        ctx['type_email'] = type_email[1]
        return TemplateResponse(request, 'person_detail.html', ctx)

    def post(self, request):
        id_person = request.POST.get("id_person")
        id_address = request.POST.get("id_address")
        id_phone = request.POST.get("id_phone")
        id_email = request.POST.get("id_email")
        if id:
            instance_person = get_object_or_404(Person, id=id_person)
            instance_address = get_object_or_404(Address, id=id_address)
            instance_phone = get_object_or_404(Phone, id=id_phone)
            instance_email = get_object_or_404(Email, id=id_email)

            person = PersonForm(request.POST or None, instance=instance_person)
            address = AddressForm(request.POST or None, instance=instance_address)
            phone = PhoneForm(request.POST or None, instance=instance_phone)
            email = EmailForm(request.POST or None, instance=instance_email)

            ctx = {"form_person": person, "form_address": address,
                   "form_phone": phone, "form_email": email,
                   "title": "Person"}
            
            return TemplateResponse(request, 'person_new.html', ctx)


class PersonNewView(TemplateView):

    def get(self, request):
        person = PersonForm()
        address = AddressForm()
        phone = PhoneForm()
        email = EmailForm()

        ctx = {"form_person": person, "form_address": address,
               "form_phone": phone, "form_email": email,
               "title": "Person"}
        return TemplateResponse(request, 'person_new.html', ctx)

    def post(self, request):
        person_form = PersonForm(request.POST)
        address_form = AddressForm(request.POST)
        phone_form = PhoneForm(request.POST)
        email_form = EmailForm(request.POST)
        if person_form.is_valid() and address_form.is_valid() and \
                phone_form.is_valid() and email_form.is_valid():
            address = address_form.save(commit=True)
            phone = phone_form.save(commit=True)
            email = email_form.save(commit=True)

            person = person_form.save(commit=False)
            person.address_id = address.pk
            person.phone_id = phone.pk
            person.email_id = email.pk
            person.save()
            return redirect('address_detail', pk=address.pk)
