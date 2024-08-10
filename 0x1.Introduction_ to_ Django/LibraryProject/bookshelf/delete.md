a = Book.objects.get(pk= 1)
a.delete()
(1, {'bookshelf.Book': 1})
Book.objects.all()
<!-- <QuerySet [<Book: Book object (1)>]> -->