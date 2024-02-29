from rest_framework import serializers
from .models import TypeLetter,Template
from letterapp.models import PdfFileTemplate


class TypeLetterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=TypeLetter
        fields=['id','name']


class TemplateSerializer(serializers.ModelSerializer):
    typeletter=TypeLetterSerializer()
    class Meta:
        model=Template
        fields=['typeletter','id','title']


class FullTemplateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Template
        fields=['id','title','body','report_date','create_date']
        read_only_fields=('title','report_date','create_date')


class TemplateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Template
        fields=['typeletter','title','body','report_date']
