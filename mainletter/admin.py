from django.contrib import admin
from .models import TypeLetter,Zarik,Template
# Register your models here.
admin.site.register([Template,TypeLetter,Zarik])