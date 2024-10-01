from django.urls import path
from .views import register, login
from .views import FollowUserAPIView,UnfollowUserAPIView, ListUsersAPIView
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('follow/<int:user_id>/', FollowUserAPIView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserAPIView.as_view(), name='unfollow_user'),
    path('users/', ListUsersAPIView.as_view(), name='list_users'),
]