from django.db import models
from letterapp.models import BaseModel
from tinymce.models import HTMLField
# Create your models here.


class TinyNoSigned(BaseModel):
    title=models.CharField(max_length=100)
    new_desc=models.TextField()