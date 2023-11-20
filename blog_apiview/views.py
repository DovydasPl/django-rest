from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Post, PostLike
from .serializers import PostSerializer, CreatePostSerializer, LoggedInUserPostSerializer, PostLikeSerializer


class PostListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Post.objects.search(query)
        return Post.objects.all()

    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        post_data = request.data
        serializer = CreatePostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Post has been created successfully!'})
        else:
            return Response(serializer.errors)
        
class PostLikeCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PostLike.objects.filter(user=self.request.user, post_id=self.kwargs['pk']).first()

    def post(self, request, *args, **kwargs):
        post_like = self.get_queryset()
        if post_like:
            post_like.delete()
            return Response({'success': 'no more like gg'})

        post_data = request.data
        serializer = PostLikeSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save(user=self.request.user, post_id=self.kwargs['pk'])
            return Response({'success': 'gg wp'})
        else:
            return Response(serializer.errors)



class PostDetailUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return get_object_or_404(Post, pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        post = self.get_queryset()
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        post = self.get_queryset()
        post.delete()
        return Response({'message': 'Post has been successfully deleted!'})

    def put(self, request, *args, **kwargs):
        post_data = request.data
        post = self.get_queryset()
        serializer = PostSerializer(post, data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class LoggedInUserPostListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return self.request.user.posts_apiview.search(query)
        return self.request.user.posts_apiview

    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = LoggedInUserPostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        post_data = request.data
        serializer = LoggedInUserPostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class LoggedInUserPostDetailUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return get_object_or_404(Post, pk=self.kwargs['pk'], user=self.request.user)

    def get(self, request, *args, **kwargs):
        post = self.get_queryset()
        serializer = LoggedInUserPostSerializer(post)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        post_data = request.data
        post = self.get_queryset()
        serializer = LoggedInUserPostSerializer(post, data=post_data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        post = self.get_queryset()
        post.delete()
        return Response({'message': 'Post has been successfully deleted!'})

