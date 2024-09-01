Book.objects.create(title = '1984', author = 'George Orwell', publication_year = '1949')
<!-- <Book: Book object (1)> -->

Book.objects.all()
<!-- <QuerySet [<Book: Book object (1)>]> -->

a= Book.objects.get(pk= 1)
a.title = 'Nineteen Eighty-Four'
a.save()
<!-- Updated -->

a = Book.objects.get(pk= 1)
a.delete()
(1, {'bookshelf.Book': 1})
Book.objects.all()
<!-- <QuerySet [<Book: Book object (1)>]> -->


