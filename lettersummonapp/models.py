from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.
MyUser=get_user_model()

class LetterSummons(BaseModel):# Chaqiruv hati

   
   letter_name=models.CharField(max_length=50)
   company_name=models.CharField(max_length=150)
   report_name=models.CharField(max_length=100)      # hisobat nomi: 1-xatdan torib oaldi
   
   user=models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True)

   adress=models.CharField(max_length=100)
   street=models.CharField(max_length=100)
   
   litter_number=models.CharField(unique=True,max_length=15)
   inn_number=models.CharField(max_length=15)
   stir_number=models.PositiveBigIntegerField(default=0)
   phone_number=models.CharField(max_length=13)
   
   report_date=models.DateTimeField()    #hisobat date: hisobat nomidan oladi
   created_date_add=models.DateTimeField(default=timezone.now()+timezone.timedelta(days=5))

   state=models.BooleanField(default=False,choices=[(True,'Topshirdi'),(False,'Topshirmadi')])

