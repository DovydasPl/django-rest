from django.contrib import admin

from .models import Post, PostLike


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'description', 'user')

class PostLikeAdmin(admin.ModelAdmin):
    model = PostLike
    list_display = ('post', 'user')


admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostLikeAdmin)
