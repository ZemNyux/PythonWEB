from datetime import date
import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import ContactInquiry


letters_only = RegexValidator(
    regex=re.compile(r'^[^\W\d_]+$', re.UNICODE),
    message='Використовуйте лише літери.',
)


class ProductComplaintForm(forms.Form):
    first_name = forms.CharField(
        label="Ім'я",
        max_length=80,
        validators=[letters_only],
        widget=forms.TextInput(attrs={'class': 'form-input', 'autocomplete': 'given-name'}),
    )
    last_name = forms.CharField(
        label='Прізвище',
        max_length=100,
        validators=[letters_only],
        widget=forms.TextInput(attrs={'class': 'form-input', 'autocomplete': 'family-name'}),
    )
    phone = forms.CharField(
        label='Контактний телефон',
        max_length=24,
        validators=[RegexValidator(r'^\+?[0-9() .-]+$', 'Введіть коректний номер телефону.')],
        widget=forms.TextInput(attrs={'class': 'form-input', 'type': 'tel', 'autocomplete': 'tel', 'placeholder': '+380 00 000 00 00'}),
    )
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-input', 'autocomplete': 'email', 'placeholder': 'name@example.com'}),
    )
    product_name = forms.CharField(
        label='Назва товару',
        max_length=180,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    purchase_date = forms.DateField(
        label='Дата придбання',
        input_formats=['%Y-%m-%d', '%d.%m.%Y'],
        widget=forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}, format='%Y-%m-%d'),
    )
    problem_description = forms.CharField(
        label='Опис проблеми',
        min_length=10,
        widget=forms.Textarea(attrs={'class': 'form-input form-textarea', 'rows': 5, 'placeholder': 'Опишіть проблему з товаром'}),
    )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if sum(character.isdigit() for character in phone) < 7:
            raise ValidationError('Номер має містити щонайменше 7 цифр.')
        return phone

    def clean_purchase_date(self):
        purchase_date = self.cleaned_data['purchase_date']
        if purchase_date > date.today():
            raise ValidationError('Дата придбання не може бути в майбутньому.')
        return purchase_date


class ContactInquiryForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше імʼя', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@example.com', 'class': 'form-input'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Тема звернення', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Коротко опишіть ваш запит',
                'class': 'form-input form-textarea',
                'rows': 5,
            }),
        }
        labels = {
            'name': 'Імʼя',
            'email': 'Email',
            'subject': 'Тема',
            'message': 'Повідомлення',
        }
