from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Flowers


class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Категория',
                                      empty_label='Все', widget=forms.Select(attrs={'class': 'form-control'}))


class MyUploadFilesForm(forms.Form):
    file = forms.FileField(label='Наш Файл')


class AddPageForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория еще не выбиралась',
                                 label='Выбор категории')

    def clean_name(self):
        name = self.cleaned_data['name']
        ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
        if not all(char in ALLOWED_CHARS for char in name):
            raise ValidationError('Не правильный ввод')
        return name

    def clean_about(self):
        about = self.cleaned_data['about']
        if len(about) < 10:
            raise ValidationError("Очень мало слов!")
        return about

    class Meta:
        model = Flowers
        fields = ['name', 'slug', 'content', 'cat', 'photo']
        labels = {'name': 'Заголовок', 'slug': 'URL', 'content': 'Информация об растении', 'photo': 'Фота'}

