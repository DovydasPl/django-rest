from django.urls import path
# from .views import LoginAPIView, RegisterAPIView, TestTokenAPIView, LoggedInUserDataAPIView
from .views import  RegisterAPIView,LoggedInUserDataAPIView

# from .views import PostList
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    # path('login/', LoginAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('test-token/', TestTokenAPIView.as_view()),
    path('user-data/', LoggedInUserDataAPIView.as_view())
]
