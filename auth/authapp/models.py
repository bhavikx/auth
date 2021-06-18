from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_user1 = models.BooleanField(default=False)
    is_user2 = models.BooleanField(default=False)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
