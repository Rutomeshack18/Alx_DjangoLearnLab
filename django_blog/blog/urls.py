from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . views import register
from . views import  profile
from .views import PostList, PostDetail, CreatePost, UpdatePost, DeletePost
from .views import home
urlpatterns = [
    path('', home, name='home'), 
    path('login/', LoginView.as_view(template_name = 'blog/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'blog/logout.html'), name = 'logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('posts/', PostList.as_view(), name = 'posts'),
    path('post/<int:pk>/', PostDetail.as_view(), name = 'postdetail'), 
    path('post/new/', CreatePost.as_view(), name = 'create'),
    path('post/<int:pk>/update/', UpdatePost.as_view(), name = 'update'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name = 'delete'),
]
