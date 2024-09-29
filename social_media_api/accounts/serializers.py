from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)  # Add the token field

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email', 'token']  # Include the token field
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create the user
        user = get_user_model().objects.create_user(**validated_data)
        # Create a token for the new user
        token = Token.objects.create(user=user)
        # Include the token in the serialized data
        user.token = token.key
        return user