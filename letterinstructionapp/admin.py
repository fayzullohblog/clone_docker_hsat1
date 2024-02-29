from django.contrib import admin
from .models import TinyNoSigned
from .forms import TinyNoSignedForm
# Register your models here.



# class TinyNoSignedAdmin(admin.ModelAdmin):
#     form=TinyNoSignedForm

# admin.site.register(TinyNoSigned,TinyNoSignedAdmin)




from tinymce.widgets import TinyMCE
from django.db import models

class TinyNoSignedAdmin(admin.ModelAdmin):
    formfield_overrides={
        models.TextField: {'widget':TinyMCE()}
    }

admin.site.register(TinyNoSigned,TinyNoSignedAdmin)


