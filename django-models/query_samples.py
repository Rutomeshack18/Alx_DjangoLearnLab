from relationship_app.models import Author, Library, Librarian

library = Library.objects.get(name=library_name)
books = library.books.all()

author = Author.objects.get(name=author_name)
books = author.books.all()

library1 = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library1)