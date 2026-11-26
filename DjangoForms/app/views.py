from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import ContactForm


def contact(request):
    """Обробка форми зворотнього зв'язку"""

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
                # красивий вивід назв полів
                label = form.fields[field_name].label or field_name
                print(f"{label:35} : {value}")

            print("=" * 60 + "\n")

            # повідомлення користувачу
            messages.success(request, 'Ваша заявка успішно надіслана! Дякуємо.')

            # залишаємось на сторінці з формою (Post/Redirect/Get для очищення полів)
            return redirect('contact')

        else:
            # якщо є помилки валідації — форма залишається заповненою, рендеримо сторінку знову
            messages.error(request, 'Будь ласка, виправте помилки у формі.')

    else:
        # GET-запит — порожня форма
        form = ContactForm()

    return render(request, 'app/contact.html', {
        'form': form,
        'title': 'Надішліть ваше повідомлення',
        'year': datetime.now().year,
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
