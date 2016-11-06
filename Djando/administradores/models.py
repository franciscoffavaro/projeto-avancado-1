from django.db import models
from django.contrib.auth.models import User

class UserAdmin(models.Model):
    user = models.OneToOneField(User)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=150)


    def __str__(self):
        return self.user.username
