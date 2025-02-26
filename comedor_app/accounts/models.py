from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id_number = models.CharField(max_length=20, unique=True)
    faculty = models.CharField(max_length=100)
    is_employee = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'id_number'
    REQUIRED_FIELDS = ['username', 'email', 'faculty']