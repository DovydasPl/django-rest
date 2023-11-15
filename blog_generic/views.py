from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from blog_apiview.models import Post
from blog_apiview.serializers import PostSerializer, LoggedInUserPostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Post.objects.search(query)
        return Post.objects.all()


class PostDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class LoggedInUserPostListCreateView(generics.ListCreateAPIView):
    serializer_class = LoggedInUserPostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return self.request.user.posts_generic

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return self.request.user.posts_generic.search(query)
        return self.request.user.posts_generic

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LoggedInUserPostDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LoggedInUserPostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return self.request.user.posts_generic
