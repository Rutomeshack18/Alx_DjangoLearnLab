from relationship_app.models import Author, Book, Library, Librarian

author=Author.objects.get(name=author_name)
books=author.books.all()

Library.objects.get(name=library_name)
books.all()

library=Library.objects.get(name=library_name)
librarian=library.librarian
