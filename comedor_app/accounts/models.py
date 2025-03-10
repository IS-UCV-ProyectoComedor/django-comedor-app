from django.contrib.auth.models import AbstractUser # type: ignore
from django.db import models # type: ignore

class UserCategory(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "User categories"

class CustomUser(AbstractUser):
    id_number = models.CharField(max_length=20, unique=True)
    faculty = models.CharField(max_length=100)
    user_category = models.ForeignKey(
        UserCategory, 
        on_delete=models.PROTECT,  # Prevent deletion of categories that have users
        null=True
    )
    
    USERNAME_FIELD = 'id_number'
    REQUIRED_FIELDS = ['username', 'email', 'faculty']