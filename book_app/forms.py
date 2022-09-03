from django.forms import ModelForm, DateInput

from .models import Book, Author


class AddBookForm(ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title' : 'Название',
            'rating' : 'Рейтинг',
            'is_best_selling' : 'Топ продаж',
            'author' : 'Автор',
            'year' : 'Год выхода', 
            'slug' : 'Slug (генерируется автоматически)',
            'description' : 'Описание',
            'image' : 'Обложка',
        }

class AddAuthorForm(ModelForm):
    
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name' : 'Имя',
            'surname' : 'Фамилия',
            'birth' : 'Дата рождения',
            'country' : 'Старана',
            'photo' : 'Фото',
        }
        widgets = {
            'birth' : DateInput(attrs={'type': 'date', 'placeholder':'-'}),
        }