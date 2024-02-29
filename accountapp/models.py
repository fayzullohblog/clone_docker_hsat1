from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin
from .userchoice import MyUserChoice
from .manager import UserManager
# Create your models here.

class MyUser(AbstractBaseUser,PermissionsMixin):
    
    username=models.CharField(max_length=50,unique=True)
    first_name=models.CharField(max_length=50,null=True,blank=True)
    last_name=models.CharField(max_length=50,null=True,blank=True)
    party_name=models.CharField(max_length=100,unique=True,null=True,blank=True)
    
    phone_number=models.CharField(max_length=30,unique=True)
    user_number_litter=models.CharField(max_length=40,unique=True,blank=True,null=True)
    image=models.ImageField(upload_to='myuser/')


    # is_admin = models.BooleanField(default=False)
    is_boss= models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

                                                                                                                                                                                   
    objects=UserManager()

    EMAIL_FIELD = "phone_number"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self) -> str:
        return self.username
    

    def full_name(self):
        return f'{self.first_name[0]}.{self.last_name}'


    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_superuser

