from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
    def create_account(self,email,first_name,last_name,password,filiation):
        if not email:
            raise ValueError(_('Please provide an email address'))
        if not first_name:
            raise ValueError(_('Please provide a first name'))
        if not last_name:
            raise ValueError(_('Please provide a last name'))
        if not password:
            raise ValueError(_('Please provide a password'))
        if not filiation:
            filiation=""

        email=self.normalize_email(email)
        user=self.model(email=email,first_name=first_name,last_name=last_name,filiation=filiation,username=email)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,first_name,last_name,password,**kwargs):
        if not email:
            raise ValueError(_('Please provide an email address'))
        if not first_name:
            raise ValueError(_('Please provide a first name'))
        if not last_name:
            raise ValueError(_('Please provide a last name'))
        if not password:
            raise ValueError(_('Please provide a password'))

        email=self.normalize_email(email)
        user=self.model(email=email,first_name=first_name,last_name=last_name,filiation="",is_staff=True,is_superuser=True,username=email)
        user.set_password(password)
        user.save()
        return user
class Account(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    username= models.CharField(_('User Name'),max_length=150)
    first_name = models.CharField(_('First Name'),max_length=150)
    last_name = models.CharField(_('last Name'),max_length=150)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    filiation = models.CharField(max_length=150,blank=True)

    objects=CustomAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    def __str__(self):
        return self.email
    

class CustomAdministratorManager(models.Manager):
    def create_administrator(self,email,first_name,last_name,password,filiation):
        account = Account.objects.create_account(email, first_name, last_name, password, filiation)
        administrator=self.model(account=account)
        administrator.save()
        return administrator


class Administrator(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE,primary_key=True)
    
    objects = CustomAdministratorManager()
    
    def __str__(self):
        return self.account.email
    
class CustomConsumerManager(models.Manager):
    def create_consumer(self,email,first_name,last_name,password,filiation):
        account = Account.objects.create_account(email, first_name, last_name, password, filiation)
        consumer=self.model(account=account)
        consumer.save()
        return consumer


class Consumer(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE,primary_key=True)
    
    objects = CustomConsumerManager()
    
    def __str__(self):
        return self.account.email
    