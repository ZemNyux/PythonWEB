from django import forms

from .models import ContactInquiry


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
