from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from ..accounts.models import User

'''
    functional user tables
'''
class service_receiver(models.Model):
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
    service_receiver_fk = models.ForeignKey(service_receiver, on_delete=models.CASCADE, null=True , blank=False)
    faq_fk =             models.ForeignKey(faq, on_delete=models.CASCADE, null=True , blank=False)
    description =        models.CharField(max_length=64, null=False, blank=True)
    price =              models.IntegerField()
    def get_id(self):
        return self.id
    def __str__(self):
        return "%s %s"%(self.id, self.price)
