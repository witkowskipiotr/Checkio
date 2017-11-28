from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django_filters.views import FilterView
from django_tables2 import RequestConfig
from django_tables2 import SingleTableMixin

from .forms import AddressForm, PersonForm, PhoneForm, EmailForm
from .models import Address, Person, Email, Phone
from group.models import GroupPerson, Group

from .tables import ListBookTable
from django_tables2 import MultiTableMixin

from django.contrib.auth.models import Group
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import ListView
from django.template import RequestContext
from guardian.decorators import permission_required_or_403, permission_required
from guardian.compat import get_user_model





#
# class Test(MultiTableMixin, TemplateView):
#
#     def get(self, request, *args, **kwargs):
#         # tables = PersonTable(Person.objects.all())
#
#         tables = [
#             Person(Person.objects.all().order_by('surname'),
#                    exclude=('address',)),
#             Person(Person.objects.all().order_by('surname'),
#                    exclude=('address', 'user',))
#         ]
#
#         ctx = {'tables': tables}
#         return render(request, 'people.html', ctx)


#
# def semantic(request):
#     '''Demonstrate the use of the Semantic UI template'''
#
#     table = ListBookTable(Person.objects.all(), order_by='-name')
#     RequestConfig(request, paginate={'per_page': 10}).configure(table)
#
#     return render(request, 'semantic_template_table.html', {
#         'table': table,
#     })

#
class ListBookView(TemplateView):

    def get(self, request, *args, **kwargs):
        table = ListBookTable(Person.objects.filter(user=request.user), order_by='-name')
        RequestConfig(request, paginate={'per_page': 10}).configure(table)

        return render(request, 'template_list.html', {
            'table': table, 'title': 'List Persons', 'link_add': 'person_new'
        })


# list_book = permission_required('address_book.view_person', return_403=True)(ListBookView.as_view())

@permission_required('address_book.view_person', return_403=True)
def list_book(request):
    table = ListBookTable(Person.objects.filter(user=request.user), order_by='-name')
    RequestConfig(request, paginate={'per_page': 10}).configure(table)

    return render(request, 'template_list.html', {
        'table': table, 'title': 'List Persons', 'link_add': 'person_new'
    })






class PersonsView(TemplateView):
    def get(self, request):



        try:
            persons = Person.objects.filter(user=request.user).order_by('surname')
        except:
            persons = None
        column_name = ['id', 'Name', 'Groups', 'Detail']
        column_data = []
        for person in persons:
            group_list = []
            for group in person.group_set.all():
                group_link = '/group/group_detail/{}'.format(group.pk)
                group_list.append(
                    {'col': group.name,
                     'link': group_link
                     }
                )

            edit_list = [

                {'col': 'View', 'link': '/address_book/person/{}'.format(person.pk)},
                {'col': 'Edit', 'link': '/address_book/person_edit/{}'.format(person.pk)},
                {'col': 'Delete', 'link': '/address_book/person_del/{}'.format(person.pk)},

            ]

            row = [
                {'col': person.id},
                {'col': person.name + '' + person.surname},
                {'many_link': group_list},
                {'many_link': edit_list},
            ]
            column_data.append(row)

        ctx = {'title': 'Persons List ({})'.format(request.user),
               'link_add': '/address_book/person_new',
               'column_name': column_name,
               'column_data': column_data
               }
        return render(request=request, template_name="forms.html",
                      context=ctx)


class PersonsAllView(TemplateView):

    def get(self, request):
        column_name = []
        column_data = []
        try:
            persons = Person.objects.all()
        except:
            persons = None

        if persons:
            column_name = [
                'id',
                'Name',
                # 'View detail'
            ]
            for person in persons:
                row = [
                    {'col': person.id},
                    {'col': person.name + '' + person.surname},
                    # {'col': 'View', 'link': '/address_book/person/{}'.format(person.pk)},
                ]
                column_data.append(row)


        ctx = {'title': 'Persons all List',
               # 'link_add': '/address_book/person_new',
               'column_name': column_name,
               'column_data': column_data
               }
        return render(request=request, template_name="forms.html",
                      context=ctx)




        # return render(request=request, template_name="persons_all.html",
        #               context={'persons': persons})


class PersonView(TemplateView):

    def get(self, request, id):
        ctx = {}
        if id:
            person = get_object_or_404(Person, id=id, user=request.user)
            # check persmission if user doesnt have permission return "no permission"
            ctx['instance'] = person

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

        ctx = {"form_person": person, "form_address": address,
               "title": "Person"}
        return TemplateResponse(request, 'person_new.html', ctx)

    def post(self, request):
        person_form = PersonForm(request.POST)
        address_form = AddressForm(request.POST)
        if person_form.is_valid() and address_form.is_valid():
            address = address_form.save(commit=True)
            person = person_form.save(commit=False)
            person.address_id = address.id
            person.user = request.user
            person.save()
            return redirect('person', id=person.id)


class PersonEditView(TemplateView):

    def get(self, request, id):
        if id:
            instance_person = get_object_or_404(Person, id=id)
            instance_address = get_object_or_404(Address, id=instance_person.address_id)

            person = PersonForm(request.POST or None, instance=instance_person)
            address = AddressForm(request.POST or None, instance=instance_address)

            ctx = {"form_person": person, "form_address": address,
                   "title": "Person", "id": id}

            return TemplateResponse(request, 'person_edit.html', ctx)

    def post(self, request, id):
        instance_person = get_object_or_404(Person, id=id)
        instance_address = get_object_or_404(Address, id=instance_person.address_id)

        person_form = PersonForm(request.POST or None, instance=instance_person)
        address_form = AddressForm(request.POST or None, instance=instance_address)

        if address_form.is_valid():
            address = address_form.save(commit=True)
        if person_form.is_valid():
            person = person_form.save(commit=False)
            person.address_id = address.id
            person.save()
            return redirect('person', id=person.id)


class PersonDelView(TemplateView):

    def get(self, request, id):
        """Method get delete person data in table address phone email and person"""
        if id:
            person = get_object_or_404(Person, id=id)
            # address = person.address
            #
            # address = get_object_or_404(Address, id=person.address_id)
            # phone = get_object_or_404(Phone, id=person.phone_id)
            # email = get_object_or_404(Email, id=person.email_id)
            #
            # if address:
            #     address.delete()
            # if phone:
            #     phone.delete()
            # if email:
            #     email.delete()
            if person:
                person.delete()

        return redirect('persons_list')

