from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
class UserManager(BaseUserManager):
    def create_user(self, password, login, phonenumber, country, city, user_type, username='' ):
        if(not phonenumber):
            raise ValueError("set phone number")

        user_obj = self.model(
            login = login,
            username = username,
            phonenumber=phonenumber,
            country=country,
            city=city,
            user_type=user_type
        )

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj
    def create_superuser(self,login, password, username, phonenumber, country, city):
        user = self.create_user(password, login, username, phonenumber, country, city, user_type=True)
        return user
'''
    Authentication
'''
class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
    (1, 'provider'),
    (2, 'reciever'),
    (3, 'stuff'),
    (4, 'supervisor'),
    (5, 'admin')
    )
    user_type =     models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    login =         models.CharField(max_length = 32, unique=True, null=False, blank=True)
    username =      models.CharField(max_length = 32, null=False, blank=True)
    phonenumber =   models.CharField(max_length = 32, null=False, blank=True)
    country =       models.CharField(max_length = 32, null=False, blank=True)
    city =          models.CharField(max_length = 32, null=False, blank=True)
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['phonenumber', 'country', 'city']
    objects = UserManager()

    def is_staff(self):
        return self.user_type==3
    def is_superuser(self):
        return self.user_type==5

    @property
    def is_user_type(self, option):
        if(self.user_type == User.USER_TYPE_CHOICES[option]):
            return True
        else:
            return False
