from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'description', 'user')


admin.site.register(Post, PostAdmin)
