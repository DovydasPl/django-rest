from django.urls import path
from .views import PostListCreateAPIView, PostDetailUpdateDeleteAPIView, LoggedInUserPostListCreateAPIView, LoggedInUserPostDetailUpdateDeleteAPIView

# from .views import PostList

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailUpdateDeleteAPIView.as_view()),
    path('posts/user/', LoggedInUserPostListCreateAPIView.as_view()),
    path('posts/user/<int:pk>/', LoggedInUserPostDetailUpdateDeleteAPIView.as_view()),
]
