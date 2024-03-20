from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Passwords(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    app_name = models.TextField(max_length = 10)
    password = models.TextField(max_length = 10)
    
    def __str__(self) -> str:
        return f"{self.user} {self.app_name} {self.password}"

