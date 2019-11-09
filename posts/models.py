from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    user_id = models.CharField(max_length=255)
    title   = models.CharField(max_length=255)
    desc    = models.TextField()
    slug    = models.TextField(null=True)
    status  = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    activation_key = models.CharField(max_length=255,default=1)
    email_validated = models.BooleanField(default=False)
    user_image = models.CharField(max_length=255,default='dummy.jpg')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User, dispatch_uid="save_new_user_profile")
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()