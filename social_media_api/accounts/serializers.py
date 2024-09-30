from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Define the custom user model
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    followers = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=get_user_model().objects.all())

    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers')

    # Create a new user and set password correctly
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
        )
        return user