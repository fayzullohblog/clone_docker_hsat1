from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model

# Create your models here
MyUser=get_user_model()

class LetterCourt(BaseModel):       # Sud hati
   letter_name=models.CharField(max_length=50)
   user=models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True) 
   litter_number=models.CharField(unique=True,max_length=15)       # 1- yoki 2- xatdan oladi
   company_name=models.CharField(max_length=150)
   ptsh=models.CharField(max_length=15)
   stir_number=models.PositiveBigIntegerField(default=0,null=True,blank=True)
   report_name=models.CharField(max_length=100)      # hisobat nomi: 2-xatdan tortib oladi
   
   report_date=models.DateTimeField() 
   company_own=models.CharField(max_length=50)                  

   def __repr__(self) -> str:
          return f'{self.letter_name} : {self.user}'

