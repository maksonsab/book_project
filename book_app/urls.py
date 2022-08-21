from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('author/<int:pk>', views.GetAuthor.as_view(), name='author_by_id'),
    path('author/add', views.AddAuthorView.as_view(), name='add_author'),
    path('book/<int:pk>', views.GetBook.as_view(), name='book_by_id'),
    path('book/<slug>', views.GetBook.as_view(), name='book_by_slug'),
    path('book/add', views.AddBookView.as_view(), name='add_book'),
    path('book/edit/<slug>', views.EditBookView.as_view(), name='edit_book'),
    path('book/delete/<int:pk>', views.DeleteBook.as_view(), name='delete_book')
    
]