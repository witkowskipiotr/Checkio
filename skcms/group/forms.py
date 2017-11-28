from django import forms
from .models import Group, GroupPerson, Person


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'alias', 'secret_key')


class GroupPersonForm(forms.ModelForm):
    class Meta:
        model = GroupPerson
        fields = ('person', 'inviter')
