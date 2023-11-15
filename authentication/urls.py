from django.urls import path
from .views import LoginAPIView, RegisterAPIView, TestTokenAPIView

# from .views import PostList

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('test-token/', TestTokenAPIView.as_view()),
]
