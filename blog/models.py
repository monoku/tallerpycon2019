from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.cache import cache


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def count_comments(self):
        # return 1
        count = cache.get(f'comments_{self.id}')
        if count is None:
            count = self.comments.count()
            cache.set(f'comments_{self.id}', count)
        return count

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
