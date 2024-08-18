from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_book, name='books'),
    path('Library/', views.LibraryDetails.as_view(), name='Library'),
]