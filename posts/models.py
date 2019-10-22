from django.db import models

class Post(models.Model):
    user_id = models.CharField(max_length=255)
    title   = models.CharField(max_length=255)
    desc    = models.TextField()
    image    = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)