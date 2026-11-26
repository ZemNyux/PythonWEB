from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('home')
    else:
        form = ContactForm()

    return render(
        request,
        'app/contact.html',
        {
            'form': form,
            'title': "Надішліть ваше повідомлення",
            'year': datetime.now().year,
        },
    )


def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        },
    )


def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        },
    )