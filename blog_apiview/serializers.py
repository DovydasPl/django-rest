from rest_framework import serializers

from .models import Post, PostLike
from authentication.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    user = UserSerializer()
    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'description',
                  'image', 'user', 'like_count', 'is_liked')

    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        else:
            return None
        
    def get_like_count(self, obj):
        return len(obj.likes.all())
    
    def get_is_liked(self, obj):
        user_like_count = len(obj.likes.filter(user=self.context.get('request').user))
        return True if user_like_count else False
        
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description',
                  'image', 'user')



class LoggedInUserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image', 'user')
        read_only_fields = ('user',)


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('user', 'post')
        read_only_fields = ('user', 'post')