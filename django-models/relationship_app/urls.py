from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import Register
urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('Library/', views.LibraryDetailView.as_view(), name='Library'),
    path('registration/', views.Register.as_view(template_name = 'registration/registration.html'), name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
]