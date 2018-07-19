from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post