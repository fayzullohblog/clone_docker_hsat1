from .models import PdfFileTemplate
# from mainletter.models import Report
from mainletter.models import Zarik
from rest_framework import serializers


class ExcelInnSerializer(serializers.Serializer):
    excel_file = serializers.FileField()


class ZarikUploadSerializer(serializers.Serializer):
    zarik_file = serializers.FileField()


class ZarikSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zarik
        fields='__all__'

# -----------------------------------------------------
class PdfFileTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model =  PdfFileTemplate
        fields = [
            'template',
            'state',
            'signed_state',
            'inn_number',
            'soato',
            'pdf_file',
            'id',
        ]


class RecentlyCreatedPdfSerializer(serializers.ModelSerializer):

    class Meta:
        model=PdfFileTemplate
        fields= [
            'pdf_file',
            'id',
        ]


class UnSignedPdfNotificationSerializer(serializers.ModelSerializer):
    signed_state=serializers.IntegerField()







