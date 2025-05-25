from django.db import models
from django.contrib.auth import get_user_model
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    image = ProcessedImageField(
        upload_to='images/',
        processors=[ResizeToFill(360, 267)],
        format='JPEG',
        options={'quality': 80},
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text[:30]


# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    class Meta:
        unique_together = ('post', 'author')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:30]