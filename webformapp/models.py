from django.db import models
from django_countries.fields import CountryField


class FormData(models.Model):
    RADIO_CHOICES = [
        ('Active Ant', 'Active Ant'),
        ('Speedy Sparrow', 'Speedy Sparrow'),
        ('Electric Elephant', 'Electric Elephant'),
    ]

    radio_buttons = models.CharField(max_length=50, choices=RADIO_CHOICES, blank=True, null=True)
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = CountryField(blank=True, null=True, default="IN")
    email_or_mobile = models.CharField(max_length=100, help_text="Enter either email or mobile")
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
