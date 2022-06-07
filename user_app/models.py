from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, full_name, email, phone, password):
        if not email:
            raise ValueError('User must have an email address')
        if not phone:
            raise ValueError('User must have a phone number')
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone=phone,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Meta:
    db_table = "AccountManager"

    def create_superuser(self, full_name, phone, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
            phone=phone,
            password=password,

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    full_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    #image = models.ImageField()
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_shopowner = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name', 'phone']

    objects = AccountManager()

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
            


class Meta:
    db_table = "User_Account"