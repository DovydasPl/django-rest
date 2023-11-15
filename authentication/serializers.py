from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']

    def create(self, validated_data):
        """ Creates and returns a new user """
        user = CustomUser(
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
