from django.contrib import admin
from .models import FormData


class FormDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'city', 'radio_buttons', 'email_or_mobile', 'remarks')


admin.site.register(FormData, FormDataAdmin)
