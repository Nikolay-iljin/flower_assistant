from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=20, label='Логин')
    password = forms.CharField(max_length=20, label='Пароль')

    class Meta():
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, label='Имя пользователя')
    password = forms.CharField(max_length=20, label='Пароль')
    password2 = forms.CharField(max_length=20, label='Повтори парль')

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name']
        labels = {'email': 'E-mail', 'first_name': 'Имя', 'last_name': 'Фамилия'}

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')

        return cd['password']

    def clean_email(self):
        cd = self.cleaned_data['email']
        if get_user_model().objects.filter(email=cd).exists():
            raise forms.ValidationError('Пользователь с таким E-mail уже существует')