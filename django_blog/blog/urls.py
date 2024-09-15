from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . views import register
from . views import  profile

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'registration/logout.html'), name = 'logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),    
]

