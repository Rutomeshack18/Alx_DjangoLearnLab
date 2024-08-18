from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('Library/', views.LibraryDetailView.as_view(), name='Library'),
]