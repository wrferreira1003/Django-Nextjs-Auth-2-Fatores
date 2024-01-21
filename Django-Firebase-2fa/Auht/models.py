from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth import get_user_model
import datetime
# Create your models here.

class User(AbstractUser):
   
     def __str__(self):
        return self.username

#Tabela para gerenciar tokens e códigos de verificação
class GerenciadorSystem(models.Model):
    User = get_user_model()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verification_codes')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Definir o tempo de expiração para 5 minutos a partir de agora
        self.expires_at = timezone.now() + datetime.timedelta(minutes=5)
        super().save(*args, **kwargs)

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at