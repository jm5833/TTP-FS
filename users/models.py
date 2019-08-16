from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    #function to create a user with an email and password
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('You must provide an email')
        if not password:
            raise ValueError('You must provide a password')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    #function to create a user with no priviledges
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    #function to create a superuser
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

#custom user class
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    current_cash = models.DecimalField(max_digits=15,
                                       decimal_places=5,
                                       default=5000.00)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
