from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render
from app.forms import ContactForm


def contact(request):
    """Обробка форми зворотнього зв'язку"""
    success = False
    has_errors = False

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # красивий вивід в консоль
            print("\n" + "=" * 60)
            print("НОВЕ ПОВІДОМЛЕННЯ З ФОРМИ ОТРИМАНО!")
            print("=" * 60)
            print(f"Дата та час: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 60)

            for field_name, value in form.cleaned_data.items():
                if value is None or value == '':
                    value = "—"
                label = form.fields[field_name].label or field_name
                print(f"{label:35} : {value}")

            print("=" * 60 + "\n")

            # очищуємо форму та вмикаємо повідомлення про успіх
            form = ContactForm()
            success = True

        else:
            has_errors = True

    else:
        form = ContactForm()

    return render(request, 'app/contact.html', {
        'form': form,
        'title': 'Надішліть ваше повідомлення',
        'year': datetime.now().year,
        'success': success,
        'has_errors': has_errors,
    })


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )
