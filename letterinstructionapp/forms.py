from django import forms
from .models import TinyNoSigned
from tinymce.widgets import TinyMCE

class TinyNoSignedForm(forms.ModelForm):
    new_desc=forms.CharField(widget=forms.Textarea(attrs={'id':'richtext_field'}))

    class Meta:
        model=TinyNoSigned
        fields='__all__'