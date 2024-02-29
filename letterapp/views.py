from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import pandas as pd
from rest_framework.permissions import AllowAny

# from mainletter.models import Report
from .models import (
                        # LetterInstruction,
                        PdfFileTemplate,
                    )
from mainletter.models import Zarik,Template
from .serializer import (
                        # LetterInstructionSerializer,
                        ExcelInnSerializer,
                        ZarikSerializer,
                        ZarikUploadSerializer,
                        PdfFileTemplateSerializer,
                        RecentlyCreatedPdfSerializer,
                        UnSignedPdfNotificationSerializer,
                        )
from rest_framework import generics, status
from django.template.loader import render_to_string

import pdfkit
from django.template.loader import get_template
from .generate_pdf import generate_pdf

class ZarikCreateApiView(generics.CreateAPIView):
    serializer_class=ZarikUploadSerializer
    queryset=Zarik.objects.all()
    permission_classes=[AllowAny]

    def post(self, request, *args, **kwargs):
        excel_file = request.data.get('zarik_file')
        try:
            df = pd.read_excel(excel_file)

            row,_=df.shape
            
            records = df.to_dict(orient='records')
            objetcs=[Zarik(**record) for record in records]
            
            Zarik.objects.bulk_create(objetcs)
            queryset=self.get_queryset()[:row]
            
            serializer=ZarikSerializer(queryset,many=True)  
            return Response({"Successful": f"{row} ta companya bazaga saqlandi"}, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            return Response({'error':f'Zarik bazani  saqlashda xatolik {e}'},status=status.HTTP_404_NOT_FOUND)


class PdfFileTemplateView(generics.CreateAPIView):
    serializer_class = ExcelInnSerializer
    queryset=PdfFileTemplate.objects.all()
    permission_classes=[AllowAny]
    
    def post(self, request, *args, **kwargs):
       
  
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():  

            excel_file=serializer.validated_data['excel_file']
            
          
            #PDF fayllaga saqlash
            
            if not excel_file:
                return Response({"error": "Excel fayli talab qilinadi."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                # Excel faylni o'qish
                df = pd.read_excel(excel_file)
                inn_number = df['inn_number'].tolist()
                # LetterInstruction obyektlarini inn_numbers bo'yicha filtrlash
              
                filtered_zarik = Zarik.objects.filter(inn_number__in=inn_number).all()
                if not filtered_zarik.exists():
                    return Response(data={'message':'Zarik baza yaratilmagan'})
              
                template_pk1=request.session.get('template_pk1')
                typeletter_pk=request.session.get('typeletter_pk')   #TODO: sesionlar saqanib qilayabdi.  
                print('------------_____>',template_pk1,typeletter_pk)      
                user=self.request.user
               
                domain_name=request.META['HTTP_HOST']
                
           
                                
                objects = []
                file_name=PdfFileTemplate.objects.pdf_file_count()
                
    
                for record in filtered_zarik:
                    file_name+=1
                    obj = PdfFileTemplate(
                        template_id=template_pk1,
             
                        inn_number=record.inn_number,
                        soato=record.soato,
                        user=user,
                        


                        pdf_file=generate_pdf(
                            template_pk1=template_pk1,
                            typeletter_pk=typeletter_pk,
                            request=request,
                            file_name=file_name,

                            adress=record.adress,
                            street=record.street,
                            company_name=record.company_name,
                            inn_number=record.inn_number,
                            phone_number=record.phone_number, 
                                                             
                            )
                    )
                    objects.append(obj)
                
                PdfFileTemplate.objects.bulk_create(objects)


                inn_count=filtered_zarik.count()
                self.request.session['count_pdf_last']=inn_count
            
                filtered_letter=PdfFileTemplate.objects.filter(inn_number__in=inn_number).all().order_by('-create_date')[:inn_count]
                serializer = PdfFileTemplateSerializer(filtered_letter, many=True)
         

                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": f"Excel faylni qayta ishlashda xato: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'Is validda xato'})


class RecentlyCreatedPdf(generics.ListAPIView):
    serializer_class = RecentlyCreatedPdfSerializer

    def get_queryset(self):
        user = self.request.user
        count_pdf_last = self.request.session.get('count_pdf_last', 0)
      
        queryset = PdfFileTemplate.objects.filter(template__user=user).order_by('-create_date')[:count_pdf_last]
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RecentlyCreatedPdfSerializer(queryset, many=True)
        return Response(serializer.data)
    
# notificartion  
class NotificationListApiView(generics.ListAPIView):

    def list(self, request, *args, **kwargs):
        queryset=PdfFileTemplate.objects.filter(signed_state=False).count()
        return Response({'meesage':{'notificatioon':queryset}})
    









def index(request):
    return render(request, 'index.html')

def tiny(request):
    return render(request=request,template_name='tiny.html')
