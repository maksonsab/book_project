from dataclasses import fields
from django import forms

from .models import Book


class AddBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title' : 'Название',
            'rating' : 'Рейтинг',
            'is_best_selling' : 'Топ продаж',
            'author' : 'Автор',
            'year' : 'Год выхода', 
            'slug' : 'Slug (генерируется автоматически)'
        }