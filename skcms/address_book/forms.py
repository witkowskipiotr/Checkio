from django import forms
from address_book.models import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('city', 'street', 'number_house', 'number_flat')


class AddressForm2(forms.ModelForm):
    city = forms.CharField(max_length=50)
    street = forms.CharField(max_length=50)
    number_house = forms.IntegerField()
    number_flat = forms.IntegerField(null=True)


class NameForm(forms.ModelForm):
    login = forms.CharField(label='Twój login', max_length=100)
