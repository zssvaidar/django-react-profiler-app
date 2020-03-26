from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
class UserManager(BaseUserManager):
    def create_user(self, password,email, username, phonenumber, country, city, user_type):
        if(not phonenumber):
            raise ValueError("set phone number")

        user_obj = self.model(
            username = username,
            phonenumber=phonenumber,
            country=country,
            email=email,
            city=city,
            user_type=user_type
        )

        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj
    def create_superuser(self,email, password, username, phonenumber, country, city):
        user = self.create_user(password,email, username, phonenumber, country, city, user_type=True)
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
'''
    functional user tables
'''
class service_reciver(models.Model):
    user =      models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    plus_code = models.CharField(max_length = 32, null=False, blank=True)

class service_provider(models.Model):
    user =      models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    login =     models.CharField(max_length = 32, null=False, blank=True)

'''
    provider identities
'''
class social(models.Model):
    provider_fk =   models.ForeignKey(service_provider, on_delete=models.CASCADE, null=True , blank=False)
    name =          models.CharField(max_length=64, null=False, blank=True)
    link =          models.CharField(max_length=64, null=False, blank=True)

'''
    service type
    maybe extended to sub categories
'''
class service_title(models.Model):
    name = models.CharField(max_length=64, null=False, blank=True)
    def __str__(self):
        return self.name

'''
    additional instructions for required service
'''
class faq(models.Model):
    name =        models.CharField(max_length=64, null=False, blank=True)
    description =        models.CharField(max_length=64, null=False, blank=True)

'''
    required service
'''
class service(models.Model):
    service_title_fk =   models.ForeignKey(service_title, on_delete=models.CASCADE, null=True , blank=False)
    service_reciver_fk = models.ForeignKey(service_reciver, on_delete=models.CASCADE, null=True , blank=False)
    faq_fk =             models.ForeignKey(faq, on_delete=models.CASCADE, null=True , blank=False)
    description =        models.CharField(max_length=64, null=False, blank=True)
    price =              models.IntegerField()
    def get_id(self):
        return self.id
    def __str__(self):
        return "%s %s"%(self.id, self.price)
