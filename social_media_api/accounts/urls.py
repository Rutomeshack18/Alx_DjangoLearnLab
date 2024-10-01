from django.urls import path
from .views import register, login
from .views import follow_user, unfollow_user, FeedView
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
    path('feed/', FeedView.as_view(), name='user_feed'),
]