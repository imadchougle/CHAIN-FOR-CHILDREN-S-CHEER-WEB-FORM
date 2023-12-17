from django import forms
from .models import FormData


class WebForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['name', 'profession', 'city', 'country', 'email_or_mobile', 'remarks', 'choice_field']