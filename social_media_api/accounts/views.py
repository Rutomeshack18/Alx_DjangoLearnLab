from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from posts.serializers import PostSerializer
from rest_framework import generics
from posts.models import Post
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # Save the user using the serializer
        
        # Explicitly create a token for the new user
        token = Token.objects.create(user=user)  # Create a new token for the user
        
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = get_user_model().objects.filter(username=username).first()

    if user and user.check_password(password):
        token, created = Token.objects.get_or_create(user=user)  # Retrieve or create token
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()

class FollowUserAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            request.user.following.add(user_to_follow)  # Add to following
            return Response({"message": "You are now following this user."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)  # Remove from following
            return Response({"message": "You have unfollowed this user."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class ListUsersAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = User.objects.all()  # Retrieve all users
        user_list = [{"id": user.id, "username": user.username} for user in users]
        return Response(user_list, status=status.HTTP_200_OK)