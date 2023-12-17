# Exercise1_WebForm/urls.py
from django.contrib import admin
from django.urls import path
from webformapp.views import webform_view, display_data_view, thank_you_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webform/', webform_view, name='webform_view'),
    path('display_data/', display_data_view, name='display_data_view'),
    path('thank_you/<int:sr_number>/', thank_you_view, name='thank_you'),
]
