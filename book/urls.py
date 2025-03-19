from django.urls import path
from book.views import BookGetAllView, BookCreateView, BookDeleteView, BookUpdateView

urlpatterns = [
    path('', BookGetAllView.as_view(), name='book_get'),
    path('add/', BookCreateView.as_view(), name='book_add'),
    path('update/<int:id>', BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:id>', BookDeleteView.as_view(), name='book_delete'),
]