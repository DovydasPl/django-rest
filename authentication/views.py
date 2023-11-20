from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from .serializers import CustomUserSerializer

User = get_user_model()



# class LoginAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         try:
#             user = User.objects.get(email=self.request.data['email'])
#         except User.DoesNotExist:
#             user = None

#         if (not user) or (not user.check_password(self.request.data['password'])):
#             return Response({"error": "Email or password is incorrect"},
#                             status=status.HTTP_404_NOT_FOUND)

#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             "data": {
#                 "token": token.key,
#                 "userData": {
#                     'id': user.id,
#                     'email': user.email
#                 }
#             }
#         })


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=request.data['email'])
            return Response({
                'data': 'mldc. hello'
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TestTokenAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]

#     def get(self, request, *args, **kwargs):
#         return Response({f"Passed for {request.user.email}"})
    
class LoggedInUserDataAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            "id": request.user.id,
            "email": request.user.email
        })

