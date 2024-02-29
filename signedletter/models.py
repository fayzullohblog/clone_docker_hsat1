from django.db import models
from utils.models import BaseModel
from accountapp.models import MyUser
# Create your models here.


class SignedPdf(BaseModel):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    pdf=models.FileField()


class UnSignedPdfurl(BaseModel):
    pdf_url=models.CharField(max_length=500)
    

