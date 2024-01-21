from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    verification_session_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
