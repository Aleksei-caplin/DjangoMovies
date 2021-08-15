from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Форма подписки по Email """

    class Meta:
        model = Contact
        fields = ("email", )
        widgets = {
            "email": forms.TextInput(attrs={"class": "editcontent", "placeholder": "Your Email ..."})
        }
        labels = {
            "email": ''
        }