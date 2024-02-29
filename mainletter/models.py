from django.db import models
from utils.models import BaseModel
from django.core.exceptions  import ValidationError
from django.core.validators import EmailValidator
from accountapp.models import MyUser
import datetime
# from django.contrib.auth import get_user_model



# User=get_user_model()


class Zarik(BaseModel):
    
    company_name=models.CharField(max_length=300)

    adress=models.CharField(max_length=300)
    street=models.CharField(max_length=300)


    phone_number=models.CharField(max_length=50)
    inn_number=models.CharField(max_length=50)

    email=models.EmailField(validators=[EmailValidator()])
    soato=models.CharField(max_length=50)

    def clean(self):
        if not (self.phone_number or self.email):
            raise ValidationError("At least one of phone number or email is required.")
        
    def __str__(self) -> str:
        return self.company_name



class TypeLetter(BaseModel):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Template(BaseModel):
    typeletter=models.ForeignKey(TypeLetter,on_delete=models.CASCADE,related_name='template')
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=150,blank=False,null=False)
    body=models.TextField(blank=False,null=False)

    report_date=models.DateField(auto_now_add=False)



    def __str__(self) -> str:
        return self.title
    

    def clean(self):
        # Ma'lumotlarni to'g'riligini tekshirish
        if self.report_date is not None and isinstance(self.report_date, str):
            try:
                # Foydalanuvchi tomonidan kiritilgan sanani "YYYY-MM-DD" formatida tekshirish
                datetime.datetime.strptime(self.report_date, "%Y-%m-%d")
            except ValueError:
                raise ValidationError("Sana noto'g'ri formatda kiritilgan. Format: YYYY-MM-DD")



