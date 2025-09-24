from django.db import models
from users.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=120)
    body = models.TextField(max_length=500,null=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    photo = models.ImageField(null=True, upload_to='static/korall/')
    name = models.CharField(max_length=120)
    email = models.EmailField(null=True)
    body = models.TextField(max_length=500,null=True)