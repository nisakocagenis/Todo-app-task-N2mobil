from django.db import models
from users.models import User

# Create your models here.

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=120)


class Photo(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE,related_name="photos")
    title = models.CharField(max_length=120)
    photo = models.ImageField(null=True, upload_to='static/korall/')
    
