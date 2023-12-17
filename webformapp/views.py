from django.shortcuts import render, redirect
from .forms import WebForm, FormData


def webform_view(request):
    if request.method == 'POST':
        form = WebForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('thank_you', sr_number=instance.id)
    else:
        form = WebForm()

    return render(request, 'webformapp/webform.html', {'form': form})


def display_data_view(request):
    form_data = FormData.objects.all()
    return render(request, 'webformapp/display_data.html', {'form_data': form_data})


def thank_you_view(request, sr_number):
    return render(request, 'webformapp/thank_you.html', {'sr_number': sr_number})