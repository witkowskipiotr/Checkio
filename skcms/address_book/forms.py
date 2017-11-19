from django import forms
from .models import Address, Phone, Email, Person


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('city', 'street', 'number_house', 'number_flat')


class PhoneForm(forms.ModelForm):
    # type = forms.ModelChoiceField(queryset=Phone.TYPE_PHONE)
    class Meta:
        model = Phone
        fields = ('number_phone', 'type')


class EmailForm(forms.ModelForm):
    # type = forms.ModelChoiceField(queryset=Email.TYPE_EMAIL,
    #         widget=forms.HiddenInput())
    class Meta:
        model = Email
        fields = ('email', 'type')


class PersonForm(forms.ModelForm):
    # address = forms.ModelChoiceField(queryset=Address.objects.all(),
    #         widget=forms.HiddenInput())
    # phone = forms.ModelChoiceField(queryset=Phone.objects.all(),
    #         widget=forms.HiddenInput())
    # email = forms.ModelChoiceField(queryset=Email.objects.all(),
    #         widget=forms.HiddenInput())

    class Meta:
        model = Person
        fields = ('name', 'surname', 'description')
                  # , 'address', 'phone', 'email')
