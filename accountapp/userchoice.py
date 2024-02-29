from django.db import models

class MyUserChoice(models.TextChoices):
    ADMIN ='admin'
    BOSS='boss'
    STAFF='staff'
    