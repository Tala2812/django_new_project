from django import forms
from .models import NewsPost

class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'short_description', 'text', 'pub_date', 'author']  # Добавлено поле author
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок новости'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите краткое описание новости'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите содержание новости'}),
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя автора'}),  # Виджет для поля author
        }