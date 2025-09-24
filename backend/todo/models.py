from django.db import models
from users.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)