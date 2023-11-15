from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    title_length = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'description',
                  'image', 'user', 'title_length')

    def get_title_length(self, obj):
        return len(obj.title)

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        else:
            return None


class LoggedInUserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image', 'user')
        read_only_fields = ('user',)
