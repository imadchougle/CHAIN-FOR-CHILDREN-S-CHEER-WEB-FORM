from django.contrib import admin
from django.urls import path
from webformapp.views import webform_view, display_data_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('webform/', webform_view, name='webform_view'),
    path('display_data/', display_data_view, name='display_data_view'),
]
