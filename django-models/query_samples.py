from relationship_app.models import Book, Librarian, Library, Author

author_books = Book.objects.get(author="author name")
library_books = Library.objects.get(name=library_name)  # "books.all()"
library_librarian = Author.objects.get(name=author_name)
library_librarian = Librarian.objects.get(library=library_name)
# objects.filter(author=author)