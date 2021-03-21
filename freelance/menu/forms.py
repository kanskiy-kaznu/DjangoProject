from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task_Models
from django.forms import ModelForm



class Create(ModelForm):
    class Meta:
        model = Task_Models
        fields = ['title', 'categories', 'descriptions', 'price']
        widgets = {"categories": forms.Select(attrs={

            'class': "form-select form-select-lg mb-3",
            'aria - label': ".form-select-lg example",

        }),
            'descriptions': forms.Textarea(attrs={

                'class': "form-control",
                'id': "floatingTextarea",
                'placeholder': 'Пример: Нужен Web-разработчик доработать проект'
            }),
            "title": forms.TextInput(attrs={
                'class': "form-control",
                'id': "floatingTextarea",
                'placeholder': 'Введите название проекта'

            }),
            'price': forms.NumberInput(attrs={
                'class': "form-control",
                'id': "floatingTextarea",

            })
        }


class LoginForms(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        'name': "your_name",
        'id': "your_name",
        'placeholder': "Имя пользователя"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type': "password",
        'name': "your_pass",
        'id': "your_pass",
        'placeholder': "Пароль",
    }))


class RegisterForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={
            'type': "text",
            'name': "name",
            'id': "name",
            'placeholder': "Имя пользователя",
        }),
            'email': forms.EmailInput(attrs={
                'type': "email",
                'name': "email",
                'id': "email",
                'placeholder': "e-mail"
            }),
            'password1': forms.PasswordInput(attrs={
                'type': "password",
                'name': "pass1",
                'id': "pass1",
                'placeholder': "Пароль",
            }),
            'password2': forms.PasswordInput(attrs={
                'type': "password",
                'name': "your_pass",
                'id': "your_pass",
                'placeholder': "Повторите пароль",
            })}
