from django.urls import path
from .views import PostListCreateView, LoggedInUserPostListCreateView, PostDetailUpdateDeleteView, LoggedInUserPostDetailUpdateDeleteView

# from .views import PostList

urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailUpdateDeleteView.as_view()),
    path('posts/user/', LoggedInUserPostListCreateView.as_view()),
    path('posts/user/<int:pk>/', LoggedInUserPostDetailUpdateDeleteView.as_view())
]
