from rest_framework import serializers
from .models import  SignedPdf
from accountapp.models import MyUser
from letterapp.models import Template,TypeLetter
from letterapp.models import PdfFileTemplate


class PartyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['party_name','username','id']


class SignedTypeLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeLetter
        fields=['name','id']


class SignedTemplateSerializer(serializers.ModelSerializer): 
    typeletter=SignedTypeLetterSerializer(read_only=True)
    username=serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model=Template
        fields=['typeletter','id','title','username']


class PdfFileTemplateUnSignedSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    template=SignedTemplateSerializer()
    

    class Meta:
        model=PdfFileTemplate
        fields=[
            'id',
            'username',
            'pdf_file',
            'template',
            'signed_state',
            'state',
        ]
        read_only_fields=(
            'id',
            'username',
            'pdf_file',
            'template',
            'signed_state',
            'titler'
        )



class PdfFileTemplateSignedSerializer(serializers.Serializer):
    ids=serializers.CharField()


    
    

    