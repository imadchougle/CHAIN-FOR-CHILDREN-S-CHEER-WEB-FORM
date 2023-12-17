# webformapp/forms.py
from django import forms
from django_countries.fields import CountryField
from .models import FormData

class WebForm(forms.ModelForm):
    # Radio button choices
    RADIO_CHOICES = [
        ('Active Ant', 'Active Ant'),
        ('Speedy Sparrow', 'Speedy Sparrow'),
        ('Electric Elephant', 'Electric Elephant'),
    ]

    # Add the new field for radio buttons
    radio_buttons = forms.ChoiceField(
        choices=RADIO_CHOICES,
        widget=forms.RadioSelect,
        label='Choose one',
    )

    class Meta:
        model = FormData
        fields = ['name', 'profession', 'city', 'country', 'email_or_mobile', 'remarks', 'radio_buttons']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['radio_buttons'].label = 'Choose one'
