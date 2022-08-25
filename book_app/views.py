from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.urls import reverse

from .models import Author, Book
from .forms import AddBookForm, AddAuthorForm

class IndexView(ListView):
    model = Book
    template_name = 'book_app/index.html'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id')[:10]
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Author.objects.order_by('-id')[:10]
        context['authors'] = authors
        context['title'] = 'Главная страница'
        return context

class GetBook(DetailView):
    model = Book
    template_name = 'book_app/book.html'
        
class AddBookView(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = 'book_app/add_new_book.html'
    success_url = '/'

class EditBookView(UpdateView):
    model = Book
    form_class = AddBookForm
    template_name = 'book_app/add_new_book.html'
    success_url = '/' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context

class DeleteBook(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'book_app/delete_book.html', context={'book': book})
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('/')

class GetAuthor(DetailView):
    model = Author
    template_name = 'book_app/author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{context["object"].name}  {context["object"].surname}'
        return context

class AddAuthorView(CreateView):
    model = Author
    form_class = AddAuthorForm
    template_name = 'book_app/add_new_author.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить автора'
        return context

class EditAuthorView(UpdateView):
    model = Author
    form_class = AddAuthorForm
    template_name = 'book_app/add_new_author.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        context['title'] = 'Изменить информацию об авторе'
        return context
    
class DeleteAuthorView(View):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        return render(request, 'book_app/delete_author.html', context={'author':author})
    
    def post(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return redirect('/')