from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from .forms import AddressForm, PersonForm, PhoneForm, EmailForm
from .models import Address, Person, Email, Phone


class PersonsView(TemplateView):
    def get(self, request):
        persons = Person.objects.all().order_by('surname')
        return render(request=request, template_name="persons.html",
                      context={'persons': persons})


class PersonView(TemplateView):
    def get(self, request, id):
        ctx = {}
        if id:
            person = Person.objects.get(id=id)
            address = Address.objects.get(id=person.address_id)
            phone = Phone.objects.get(id=person.phone_id)
            email = Email.objects.get(id=person.email_id)
            if person:
                ctx['id'] = person.id
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
        return TemplateResponse(request, 'person.html', ctx)

    def post(self, request): #TODO ?
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
            person.address_id = address.id
            person.phone_id = phone.id
            person.email_id = email.id
            person.save()
            return redirect('person', id=person.id)


class PersonEditView(TemplateView):

    def get(self, request, id):
        if id:
            instance_person = get_object_or_404(Person, id=id)
            instance_address = get_object_or_404(Address, id=instance_person.address_id)
            instance_phone = get_object_or_404(Phone, id=instance_person.phone_id)
            instance_email = get_object_or_404(Email, id=instance_person.email_id)

            person = PersonForm(request.POST or None, instance=instance_person)
            address = AddressForm(request.POST or None, instance=instance_address)
            phone = PhoneForm(request.POST or None, instance=instance_phone)
            email = EmailForm(request.POST or None, instance=instance_email)

            ctx = {"form_person": person, "form_address": address,
                   "form_phone": phone, "form_email": email,
                   "title": "Person", "id": id}

            return TemplateResponse(request, 'person_edit.html', ctx)

    def post(self, request, id):
        instance_person = get_object_or_404(Person, id=id)
        instance_address = get_object_or_404(Address, id=instance_person.address_id)
        instance_phone = get_object_or_404(Phone, id=instance_person.phone_id)
        instance_email = get_object_or_404(Email, id=instance_person.email_id)

        person_form = PersonForm(request.POST or None, instance=instance_person)
        address_form = AddressForm(request.POST or None, instance=instance_address)
        phone_form = PhoneForm(request.POST or None, instance=instance_phone)
        email_form = EmailForm(request.POST or None, instance=instance_email)

        if address_form.is_valid():
            address = address_form.save(commit=True)
        if phone_form.is_valid():
            phone = phone_form.save(commit=True)
        if email_form.is_valid():
            email = email_form.save(commit=True)
        if person_form.is_valid():
            person = person_form.save(commit=False)
            person.address_id = address.id
            person.phone_id = phone.id
            person.email_id = email.id
            person.save()
            return redirect('person', id=person.id)


class PersonDelView(TemplateView):

    def get(self, request, id):
        """Method get delete person data in table address phone email and person"""
        if id:
            person = get_object_or_404(Person, id=id)
            # address = person.address

            address = get_object_or_404(Address, id=person.address_id)
            phone = get_object_or_404(Phone, id=person.phone_id)
            email = get_object_or_404(Email, id=person.email_id)

            if address:
                address.delete()
            if phone:
                phone.delete()
            if email:
                email.delete()
            if person:
                person.delete()

        return redirect('persons')

