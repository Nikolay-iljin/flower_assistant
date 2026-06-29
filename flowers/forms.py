from django import forms
from .models import Category


class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Категория', empty_label='Все', widget=forms.Select(attrs={'class': 'form-control'}))
