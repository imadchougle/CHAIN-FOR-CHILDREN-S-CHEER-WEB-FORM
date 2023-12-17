from django.contrib import admin
from django.urls import path
from webformapp.views import webform_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('webform/', webform_view, name='webform_view'),
]