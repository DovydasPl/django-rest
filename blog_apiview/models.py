from django.db import models
from django.conf import settings
from django.db.models import Q


class PostQuerySet(models.QuerySet):
    def search(self, query):
        lookups = Q(title__icontains=query) | Q(description__icontains=query)
        return self.filter(lookups)


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='posts_apiview')
    image = models.ImageField(upload_to='covers', null=True, blank=True)

    objects = PostQuerySet().as_manager()

class PostLike(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)