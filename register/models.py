from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class Gender(models.IntegerChoices):
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'
    OTHER = 3, 'Other'



class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("The Email field must be set")
        phone = self.normalize_email(phone)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone, password, **extra_fields)

# models.py

class CustomUser(models.Model):
    phone = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=True)
    gender = models.IntegerField(choices=Gender.choices, null=True)
    country = models.CharField(max_length=100, null=True, blank=True)  # <-- changed
    city = models.CharField(max_length=100, null=True, blank=True)     # <-- changed
    
    def __str__(self):
        return f"{self.phone} - {self.first_name or ''} {self.last_name or ''}"


class UserResponse(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='responses')
    concept = models.CharField(max_length=100, null=True)  # ✅ Add this
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Response from {self.user.phone} at {self.created_at}"
