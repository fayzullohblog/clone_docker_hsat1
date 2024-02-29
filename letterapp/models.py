from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from datetime import timedelta
from utils.models import BaseModel
from mainletter.models import Template,TypeLetter
# Create your models here.
MyUser=get_user_model()


# Upload pdf file for LetterInstruction
class PdfFilePath(models.TextChoices):
    pdf_instraction_path='pdfletterinstruction/unsigned/'

# Manager Count Class for Pdf file fields
class PdfFileLetterinstructionManager(models.Manager):
    def pdf_file_count(self):
        return self.values('pdf_file').count()

class NotificationManager(models.Manager):
    def signed_state_count(self):
        signed_state_count=self.filter(signed_state=False).count()
        return signed_state_count


class PdfFileTemplate(BaseModel):  # Ko'rstma hati1
   
   template=models.ForeignKey(Template,on_delete=models.CASCADE,related_name='pdffiletemplate_template')
   user=models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name='pdffiletemplate_user')

   pdf_file=models.FileField(upload_to=PdfFilePath.pdf_instraction_path)
   
   soato=models.CharField(max_length=50)
   inn_number=models.CharField(max_length=15) 
   
   letter_date=models.DateTimeField(default=timezone.now()+timedelta(days=7))
   
   state=models.BooleanField(default=False,choices=[(True,'Topshirdi'),(False,'Topshirmadi')])
   signed_state=models.BooleanField(default=False)
   

   objects=PdfFileLetterinstructionManager()


   def letter_date(self):
       date=self.template.update_date
       return date
   



   
   
