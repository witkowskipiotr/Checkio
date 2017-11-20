from django import forms
from address_book.models import Group, GroupPerson


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name',)


class GroupPersonForm(forms.ModelForm):
    class Meta:
        model = GroupPerson
        fields = ('person', 'group',)
