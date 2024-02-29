from django.shortcuts import render
from rest_framework import generics

from django.shortcuts import get_object_or_404

from .serializer import TypeLetterSerializer,TemplateSerializer,FullTemplateSerializer,TemplateCreateSerializer
from .models import TypeLetter,Template
from accountapp.models import MyUser

from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import AllowAny
import datetime
from django.core.exceptions  import ValidationError
#  Create your views here.


class TypleLetterListApiView(generics.ListAPIView):
    serializer_class=TypeLetterSerializer
    queryset=TypeLetter.objects.all()
    permission_classes=[AllowAny]



class TemplateRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()
    permission_classes=[AllowAny]

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')

        template_instance = self.queryset.filter(typeletter__id=pk,user=self.request.user).all()
        
        serializer = self.serializer_class(template_instance,many=True)

        return Response(serializer.data)
    


class TemplateRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = FullTemplateSerializer
    queryset = Template.objects.all()
    permission_classes=[AllowAny]


    def get(self, request, *args, **kwargs):
        template_pk1 = self.kwargs.get('pk1')
        typeletter_pk = self.kwargs.get('pk')
        user=request.user
        
        
        if template_pk1 is None or typeletter_pk is None:
            return Response({'status': 'don\'t gave name id'}, status=status.HTTP_400_BAD_REQUEST)


        try:
            typeletter = get_object_or_404(TypeLetter, id=typeletter_pk)
            template_instance = get_object_or_404(self.queryset, typeletter__name=typeletter, id=template_pk1,user=user)

            serializer = self.serializer_class(template_instance)
            return Response(serializer.data)
        except:
            return Response({'message':'Bu turdagi xisoblar ruyxati mavjud emas'})
    

    def put(self, request, *args, **kwargs):
        template_pk1 = self.kwargs.get('pk1')
        typeletter_pk = self.kwargs.get('pk')

        if template_pk1 is None or typeletter_pk is None:
            return Response({'status': 'don\'t gave name id'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:

            typeletter = get_object_or_404(TypeLetter, id=typeletter_pk)
            template_instance = get_object_or_404(self.queryset, typeletter__name=typeletter, id=template_pk1)
            
            request.session['template_pk1']=template_instance.id
            request.session['typeletter_pk']=typeletter.id


            body_data = request.data.get('body', None)

            if body_data is not None:
                template_instance.body = body_data
                template_instance.save()

            serializer = self.serializer_class(template_instance, partial=True)
            return Response(serializer.data)

        except:
            return Response({'message':'Mavjud bulmagan xisob ruyxati uchun , xech nimani o\'zgartira olmaysiz'})
           
       

class TemplateCreateView(generics.CreateAPIView):
    queryset=Template.objects.all()
    serializer_class=TemplateCreateSerializer
    permission_classes=[AllowAny]
   
    def create(self, request, *args, **kwargs):
        
        user=self.request.user
        typeletter_id=self.request.data.get('typeletter')

        title=self.request.data.get('title')
        body=self.request.data.get('body')
        report_date=self.request.data.get('report_date',None)
        
        try:

            typeletter_instance=TypeLetter.objects.get(id=typeletter_id)
            
        except TypeLetter.DoesNotExist:

            return Response({'error':'Invalid typeletter ID '}, status=400)
        
        
        if not bool(title) or title.isspace() or not bool(body) or body.isspace():
            return Response({"message":'biror maydondi bush qoldirdingizmi?'})

        elif not bool(report_date):
            return Response({"message":'Xisobat sanasini kiriting!!'})

        else:
            query=Template.objects.create(
                typeletter=typeletter_instance,
                user=user,
                title=title,
                body=body,
                report_date=report_date,
            )
            serializer=self.serializer_class(query)
        

        return Response(serializer.data)








    

    

    


    
    





    



    




    
    











    
