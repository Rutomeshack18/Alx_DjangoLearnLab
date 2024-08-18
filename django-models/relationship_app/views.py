from typing import Any
from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView
# Create your views here.
def list_book(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetails(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context ['books'] = library.books.all()

