from django import forms
from django.core.validators import MinLengthValidator


class ContactForm(forms.Form):
    """Розширена форма для демонстрації різних полів і віджетів Django"""

    # текстові поля
    full_name = forms.CharField(
        label="ПІБ",
        max_length=150,
        validators=[MinLengthValidator(3)],
        widget=forms.TextInput(attrs={
            'class': 'form-control', # bootstrap-клас для стилізації
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
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+380 XX XXX XX XX',
            'type': 'tel'
        })
    )

    # числові поля
    age = forms.IntegerField(
        label="Ваш вік",
        min_value=16,
        max_value=100,
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    budget = forms.DecimalField(
        label="Приближний бюджет (грн)",
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '100'
        })
    )

    # дата
    preferred_date = forms.DateField(
        label="Бажана дата консультації",
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    # вибір (одне значення)
    GENDER_CHOICES = [
        ('male', 'Чоловіча'),
        ('female', 'Жіноча'),
        ('other', 'Інше'),
    ]

    gender = forms.ChoiceField(
        label="Стать",
        choices=GENDER_CHOICES,
        required=False,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    CONTACT_METHOD_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Телефон'),
        ('telegram', 'Telegram'),
    ]

    preferred_contact = forms.ChoiceField(
        label="Найзручніший спосіб зв'язку",
        choices=CONTACT_METHOD_CHOICES,
        initial='email',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # множинний вибір
    INTEREST_CHOICES = [
        ('web_dev', 'Веб-розробка'),
        ('mobile', 'Мобільна розробка'),
        ('design', 'Дизайн'),
        ('marketing', 'Маркетинг'),
        ('business', 'Бізнес-консультація'),
        ('other', 'Інше'),
    ]

    interests = forms.MultipleChoiceField(
        label="Цікавить (можна обрати кілька)",
        choices=INTEREST_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    # булеве поле
    newsletter = forms.BooleanField(
        label="Хочу отримувати корисну розсилку",
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    # текстове поле з валідацією
    message = forms.CharField(
        label="Повідомлення / питання",
        min_length=20,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Опишіть ваше питання або побажання...'
        })
    )

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message and len(message.strip()) < 20:
            raise forms.ValidationError("Повідомлення повинно містити хоча б 20 символів.")
        return message.strip()