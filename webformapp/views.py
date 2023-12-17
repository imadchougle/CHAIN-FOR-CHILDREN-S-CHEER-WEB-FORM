from django.shortcuts import render, redirect
from .forms import WebForm


def webform_view(request):
    if request.method == 'POST':
        form = WebForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webform_view')
    else:
        form = WebForm()

    return render(request, 'webformapp/webform.html', {'form': form})