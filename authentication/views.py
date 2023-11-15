from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from .serializers import CustomUserSerializer

User = get_user_model()


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=self.request.data['email'])
        except User.DoesNotExist:
            user = None

        if (not user) or (not user.check_password(self.request.data['password'])):
            return Response({"error": "Email or password is incorrect"},
                            status=status.HTTP_404_NOT_FOUND)

        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=request.data['email'])
            token = Token.objects.create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestTokenAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        return Response({f"Passed for {request.user.email}"})
