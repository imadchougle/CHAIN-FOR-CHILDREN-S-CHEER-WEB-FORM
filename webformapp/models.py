# webformapp/models.py
from django.db import models
from django_countries.fields import CountryField


class FormData(models.Model):
    ANT = 'Active Ant'
    SPARROW = 'Speedy Sparrow'
    ELEPHANT = 'Electric Elephant'

    CHOICES = [
        (ANT, 'Active Ant'),
        (SPARROW, 'Speedy Sparrow'),
        (ELEPHANT, 'Electric Elephant'),
    ]

    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = CountryField(blank=True, null=True)
    email_or_mobile = models.CharField(max_length=100, help_text="Enter either email or mobile")
    remarks = models.TextField(blank=True, null=True)
    choice_field = models.CharField(max_length=50, choices=CHOICES, default=ANT)

    def __str__(self):
        return self.name
