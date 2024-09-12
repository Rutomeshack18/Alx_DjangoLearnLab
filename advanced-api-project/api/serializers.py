from rest_framework import serializers
from . models import Book, Author
import datetime

# The AuthorSerializer uses a nested BookSerializer to  show the one to many relationship between book and author
# A validation is added to the BookSerializer to ensure the publication date is not in the future

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year','author']

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('Publication year cannot be in the future')
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many = True, read_only = True)
    class Meta:
        model = Author
        fields = ['name', 'books']
