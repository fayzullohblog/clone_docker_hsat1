from rest_framework import serializers
from .models import TinyNoSigned


class LetterInstructionNoSignedSerializer(serializers.ModelSerializer):
    class Meta:
        model=TinyNoSigned
        fields=['tiny_field']


class LetterTemplatesserializer(serializers.Serializer):
    templates=serializers.CharField()

