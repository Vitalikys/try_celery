from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='User Name or any text')
    email = forms.CharField(label='send to my mail@address :')

    class Meta:
        model = Contact
        fields = '__all__'
