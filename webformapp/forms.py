from django import forms
from .models import FormData


class WebForm(forms.ModelForm):
    RADIO_CHOICES = [
        ('Active Ant', 'Active Ant'),
        ('Speedy Sparrow', 'Speedy Sparrow'),
        ('Electric Elephant', 'Electric Elephant'),
    ]

    radio_buttons = forms.ChoiceField(
        choices=RADIO_CHOICES,
        widget=forms.RadioSelect,
        label='Choose one',
    )

    class Meta:
        model = FormData
        fields = ['radio_buttons', 'name', 'profession', 'city', 'country', 'email_or_mobile', 'remarks']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['radio_buttons'].label = 'I would like to be:'
