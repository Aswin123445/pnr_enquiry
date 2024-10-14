from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,name,sur_name,password=None,is_active=True,is_staff=False,is_superuser=False):
        if not email:
            raise ValueError("the email field must be set")
        email=self.normalize_email(email)
        user=self.model(
            email=email,
            name=name,
            sur_name=sur_name,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        user.set_password(password)  
        user.save() 
        return user

class UserData(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
        null=False,
        verbose_name='User\'s email address',
        help_text='Enter a valid emaail address'
    )
    name = models.CharField(
        max_length=30
    )
    sur_name=models.CharField(
        max_length=30
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects=UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'sur_name']

    def __str__(self):
        return self.email

