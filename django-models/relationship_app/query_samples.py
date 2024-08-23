from .models import Author, Book, Library, Librarian

#Creating author field
author_name = Author.objects.create(name="Meshack Ruto")
author_name.save()
author = "Meshack Ruto"

#Querying all books by a specific author
Author.objects.get(name=author_name)
Author.objects.filter(author=author)

#Adding titles of the Book
Last = Book.objects.create(title="River and the Source")
Last.save()
#Filtering books by author
Book.objects.get(author=author_name)

#Library
one_library = Library.objects.create(name="one_library")

#Adding Books to the Library
one_library.books.add(Last)

#Listing all books in a Library
one_library.books.all()
one_library.objects.get(name=one_library)

#Adding a Librarian
library_name = Librarian.objects.create(name="first", library=one_library)
library_name.save()

#Retrieving a Librarian
Librarian.objects.get(library= one_library)

#Listing all books
Library.objects.get(name=library_name)
books = Book.objects.all()