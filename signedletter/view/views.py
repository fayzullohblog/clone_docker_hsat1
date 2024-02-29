from django.shortcuts import render
from rest_framework import  generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from ..models import SignedPdf
from letterapp.models import PdfFileTemplate
from accountapp.models import MyUser
from letterapp.models import Template,TypeLetter
from rest_framework import status
from ..serializer import (
                PartyUserSerializer,
                SignedTemplateSerializer,
                SignedTypeLetterSerializer,
                PdfFileTemplateUnSignedSerializer,
                # PdfFileTemplateUnsignedSerializer,
                PdfFileTemplateSignedSerializer,
                 )     
from ..persmissions import OnlySuperUserOrStaff
from rest_framework.permissions import IsAuthenticated

from ..pdf_parser import PdfParser
from config.settings import MEDIA_ROOT
import os
# Create your views here.



class PartyUserListApiView(generics.ListAPIView):
    serializer_class=PartyUserSerializer
    queryset=MyUser.objects.all()
    permission_classes=[IsAuthenticated,OnlySuperUserOrStaff]
    

    def get(self, request, *args, **kwargs):
        queryset=self.queryset.filter(is_staff=True,is_superuser=False,is_active=True)
        serializer=self.serializer_class(queryset,many=True).data
        return Response({'result':serializer})


class TypeLetterListApiView(generics.ListAPIView):
    serializer_class=SignedTypeLetterSerializer
    queryset=TypeLetter.objects.all()
    permission_classes=[IsAuthenticated,OnlySuperUserOrStaff]

    def get(self, request, *args, **kwargs):    
        request.session['staff_username']=self.kwargs['staff_username']
        return super().get(request, *args, **kwargs)


    
    


class TemplateListApiView(generics.ListAPIView):
    serializer_class=SignedTemplateSerializer
    queryset=Template.objects.all()



    def get(self, request, *args, **kwargs):
        typeletter_id=self.kwargs['pk']
        try:
            staff_username=request.session['staff_username']
            
        except:
            return Response("Siz bo'limdi tanlamasdan, xatlar turini ko'ra olmaysiz, birinchi  bo'limni tanlang keyin xatlarni ko'ra olasiz")
        

        queryset=self.queryset.filter(typeletter_id=typeletter_id,user__username=staff_username).all()
        serializer=self.serializer_class(instance=queryset,many=True)
        
        return Response(serializer.data)


class PdfFileTemplateUnsignedListApiView(APIView):
    serializer_class=PdfFileTemplateUnSignedSerializer


    def get_queryset(self):
        # queryset = PdfFileTemplate.objects.all()
        return PdfFileTemplate.objects.all()
    
    def get(self, request, *args, **kwargs):
        template_pk1 = self.kwargs.get('pk1')
        typeletter_pk = self.kwargs.get('pk')
        
        if template_pk1 is None or typeletter_pk is None:
            return Response({'status': 'don\'t gave name id'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            staff_username=request.session['staff_username']
        except:
            return Response("Siz bo'limdi tanlamasdan, bo'limga tegishli xisobatlarni ko'ra olmaysiz, birinchi  bo'limni tanlang keyin xatlarni ko'ra olasiz")
        
        
        pdffiletemplate=self.get_queryset().filter(
            template_id=template_pk1,
            user__username=staff_username,
            signed_state=False,
            template__typeletter_id=typeletter_pk)

        serializer = self.serializer_class(pdffiletemplate,many=True)
        return Response(serializer.data)


class PdfFileTemplateUnsignedDestroyApiView(generics.RetrieveDestroyAPIView):
    serializer_class=PdfFileTemplateUnSignedSerializer
    queryset = PdfFileTemplate.objects.all()





class PdfFileTemplateSignedUpdateApiView(APIView):
    

    def put(self, request, *args, **kwargs):
        try:
            data = request.data
            pdf_file_updates = data.get('pdf_file_updates', [])  # List of dictionaries with 'id', 'pdf_file', and 'signed_state'

            domain_name=request.META['HTTP_HOST']
            for update_data in pdf_file_updates:
                pdf_file_id = update_data.get('id')
                # pdf_file_path = update_data.get('pdf_file')
                signed_state = update_data.get('signed_state')

                try:
                    pdf_file_instance = PdfFileTemplate.objects.get(id=pdf_file_id,signed_state=signed_state)
                    
                except PdfFileTemplate.DoesNotExist:
                    return Response({'status': f'PdfFileTemplate with id {pdf_file_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)

                pdf_file_path=pdf_file_instance.pdf_file.path
                pdf_file_name=pdf_file_path.split('/')[-1]
                new_folder_name=pdf_file_instance.user

                
              
                new_folder = os.path.join(MEDIA_ROOT,new_folder_name.username)
               

                if not  os.path.exists(new_folder):
                    os.mkdir(new_folder)
                
                user=self.request.user
                pdf_file=PdfParser(pdf_file_path,domain_name,user)
              
                pdf_file.create_pdf(
                                save_folder_path=new_folder,
                                # page=pdf_file_id,
                                page=pdf_file_name,

                                data_1=request.user.first_name, 
                                x_path_1=420, y_path_1=130,

                                data_2=request.user.username,
                                x_path_2=80, y_path_2=130
                                )
                
                SignedPdf.objects.create(user=new_folder_name,pdf=f'{new_folder_name.username}/{pdf_file_name}')
                pdf_file_instance.signed_state=True
                pdf_file_instance.save()

                


            return Response({'status': 'Successfully updated'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'status': f'Error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class PdffileTemplateUpdateStateField(generics.RetrieveUpdateAPIView):
    pass


class PdfFileTemplateStateFieldListApiview(generics.ListAPIView):
    pass
    



# {
#     "pdf_file_updates": [
#         {"id": 83, "signed_state": false},
#         {"id": 84, "signed_state": false}
#     ]
# }



# {
#     "pdf_file_updates": [
#         {"id": 79, "signed_state": false}
#     ]
# }
        


