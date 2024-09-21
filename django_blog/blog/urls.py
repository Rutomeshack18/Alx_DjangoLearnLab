from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . views import register
from . views import  profile
from .views import PostList, PostDetail, CreatePost, UpdatePost

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'blog/templates/blog/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('posts/', PostList.as_view(), name = 'posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name = 'postdetail'), 
    path('posts/new/', CreatePost.as_view(), name = 'create'),
    path('posts/<int:pk>/edit/', UpdatePost.as_view(), name = 'update')
]
