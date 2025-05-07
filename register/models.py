# settings.py must already include USE_I18N = True and LANGUAGES, LOCALE_PATHS, etc.

# --- register/models.py ---
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.IntegerChoices):
    MALE = 1, _('Male')
    FEMALE = 2, _('Female')
    OTHER = 3, _('Other')


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError(_('The phone number must be set'))
        phone = self.normalize_email(phone)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)


class CustomUser(models.Model):
    phone = models.CharField(_('Phone Number'), max_length=12, unique=True)
    first_name = models.CharField(_('First Name'), max_length=30, null=True, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, null=True, blank=True)
    age = models.IntegerField(_('Age'), null=True)
    gender = models.IntegerField(_('Gender'), choices=Gender.choices, null=True)
    country = models.CharField(_('Country'), max_length=100, null=True, blank=True)
    city = models.CharField(_('City'), max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.phone} - {self.first_name or ''} {self.last_name or ''}"


class UserResponse(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='responses', verbose_name=_('User'))
    concept = models.CharField(_('Concept'), max_length=100, null=True)
    text = models.TextField(_('Response'))
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    def __str__(self):
        return f"Response from {self.user.phone} at {self.created_at}"