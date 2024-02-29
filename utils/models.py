from django.db import models
from django.utils import timezone



class BaseModel(models.Model):
    create_date=models.DateTimeField(auto_now=True,blank=True)  #+ 30, shanbni , yakshanbi  bulsa, dushanbiga utish kerak   
    update_date=models.DateTimeField(auto_now_add=True,blank=True)

    class Meta:
        abstract=True

