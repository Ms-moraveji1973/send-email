from django import forms
from .models import EmailModel

class EmailForms(forms.ModelForm):
    class Meta:
        model = EmailModel
        fields = ['email', 'subject', 'content',]

