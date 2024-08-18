# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.
author = Author.objects.get(name= 'author_name')
books = author.books.all()

library = Library.objects.get(name= 'library_name')
books = library.books.all()

library = Library.objects.get(name = 'Library_name')
librarian = Librarian.objects.get(library=library)