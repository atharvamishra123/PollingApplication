from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from user.manager import UserManager


# Create your models here.
class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=250, null=False)
    password = models.CharField(max_length=15, null=False)
    username = models.CharField(max_length=15, null=False, unique=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email + ',' + str(self.is_admin) + ',' + str(self.is_superuser) + str(self.is_active) + ',' + str(
            self.is_staff) + str(self.password)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
