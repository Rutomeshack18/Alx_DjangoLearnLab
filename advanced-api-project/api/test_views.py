from rest_framework.test import APITestCase
from rest_framework import status
from . models import Book
from . models import Author
from django.contrib.auth.models import User


class BookTestCase(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='Author Name')

    def test_create_book(self):
        url = '/api/books/create/'
        data = {'title': 'River and the Source', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'River and the Source')
    
    def test_update_book(self):
        url = '/api/books/update/'
        data = {'title': 'River Between', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get().title, 'River Between')

    def test_delete_book(self):
        url= '/api/books{book_id}/delete/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    
    def test_permissions(self):
        self.client.logout()
        url = '/api/books/create/'
        data = {'title': 'Unauthorized Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)