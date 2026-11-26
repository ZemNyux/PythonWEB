# Forms

перевірка даних форми Django 

from django import forms
from django.core.validators import MinLengthValidator, RegexValidator
from datetime import date

# звісно, існують і бібліотеки для валідації форм, наприклад django-crispy-forms + crispy-bootstrap5
# pydantic (з Django Ninja або самостійно), або django-bootstrap5
# https://django-crispy-forms.readthedocs.io/en/latest/
# встановлення: pip install django-crispy-forms crispy-bootstrap5

# https://pydantic.dev/docs/validation/latest/get-started/
# https://django-bootstrap5.readthedocs.io/en/latest/forms.html

# приклад кастомного валідатора
def validate_phone(value):
    """Кастомний валідатор для телефону"""
    import re
    if value and not re.match(r'^\+?380\d{9}$', value.replace(' ', '').replace('(', '').replace(')', '')):
        raise forms.ValidationError("Введіть коректний номер телефону у форматі +380XXXXXXXXX")


class ContactForm(forms.Form):
    """Розширена форма з різними рівнями валідації"""

    full_name = forms.CharField(
        label="ПІБ",
        max_length=150,
        validators=[MinLengthValidator(3)],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Шевченко Тарас Григорович'
        })
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'shevchenko.t@gmail.com'
        })
    )

    phone = forms.CharField(
        label="Телефон",
        max_length=20,
        required=False,
        validators=[validate_phone],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+380 XX XXX XX XX',
            'type': 'tel'
        })
    )

    preferred_date = forms.DateField(
        label="Бажана дата консультації",
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    preferred_contact = forms.ChoiceField(
        label="Найзручніший спосіб зв'язку",
        choices=[
            ('email', 'Email'),
            ('phone', 'Телефон'),
            ('telegram', 'Telegram'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    interests = forms.MultipleChoiceField(
        label="Цікавить (можна обрати кілька)",
        choices=[
            ('web_dev', 'Веб-розробка'),
            ('mobile', 'Мобільна розробка'),
            ('design', 'Дизайн'),
            ('marketing', 'Маркетинг'),
            ('business', 'Бізнес-консультація'),
        ],
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )
    
    # interests = forms.MultipleChoiceField(
    # label="Цікавить (можна обрати кілька)",
    #     choices=[
    #         ('web_dev', 'Веб-розробка'),
    #         ('mobile', 'Мобільна розробка'),
    #         ('design', 'Дизайн'),
    #         ('marketing', 'Маркетинг'),
    #         ('business', 'Бізнес-консультація'),
    #     ],
    #     required=False,
    #     widget=forms.SelectMultiple(attrs={ # випадаючий список з можливістю обрати декілька пунктів одночасно
    #         'class': 'form-select',
    #         'size': 5,           # кількість видимих рядків
    #  })
    # )

    newsletter = forms.BooleanField(
        label="Хочу отримувати корисну розсилку",
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    message = forms.CharField(
        label="Повідомлення / питання",
        min_length=20,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Опишіть ваше питання або побажання...'
        })
    )

    # !!!!! валідація на рівні поля

    def clean_email(self):
        """Приклад валідації конкретного поля"""
        email = self.cleaned_data.get('email')
        if email and email.endswith('@example.com'):
            raise forms.ValidationError("Реальні email з доменом @example.com заборонені.")
        return email

    def clean_preferred_date(self):
        """Перевірка, що дата не в минулому"""
        preferred_date = self.cleaned_data.get('preferred_date')
        if preferred_date and preferred_date < date.today():
            raise forms.ValidationError("Бажана дата не може бути в минулому.")
        return preferred_date

    def clean_message(self):
        """Валідація повідомлення"""
        message = self.cleaned_data.get('message')
        if message and len(message.strip()) < 20:
            raise forms.ValidationError("Повідомлення повинно містити хоча б 20 символів.")
        return message.strip()

    # !!!!! загальна валідація (clean)

    def clean(self):
        """Загальна валідація форми — перевірка декількох полів разом"""
        cleaned_data = super().clean()

        message = cleaned_data.get('message')
        interests = cleaned_data.get('interests')
        preferred_contact = cleaned_data.get('preferred_contact')

        # якщо людина не вказала інтереси і не написала повідомлення
        if not interests and (not message or len(message) < 30):
            raise forms.ValidationError(
                "Будь ласка, або оберіть хоча б одну послугу, або детальніше опишіть ваше питання."
            )

        # якщо обрали телефон як спосіб зв'язку - телефон обов'язковий
        if preferred_contact == 'phone' and not cleaned_data.get('phone'):
            self.add_error('phone', "Якщо ви обрали телефон як спосіб зв'язку, вкажіть номер.")

        return cleaned_data
