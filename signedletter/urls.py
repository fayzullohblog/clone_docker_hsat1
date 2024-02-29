from django.urls import path
from .view.views import (
            TemplateListApiView,
            PartyUserListApiView,
            TypeLetterListApiView,
            PdfFileTemplateUnsignedListApiView,
            PdfFileTemplateUnsignedDestroyApiView,
            PdfFileTemplateSignedUpdateApiView,
            )
urlpatterns = [
    path('partyuser/',PartyUserListApiView.as_view()),
    path('partyuser/<str:staff_username>/typeletter/',TypeLetterListApiView.as_view()),
    path('partyuser/typeletter/<int:pk>/',TemplateListApiView.as_view()), # TODO: session key saqlanib qolayabdi shu urlda: jahongir nomi bilan
    path('partyuser/typeletter/<int:pk>/<int:pk1>/',PdfFileTemplateUnsignedListApiView.as_view()),
    path('partyuser/typeletter/pdffiletemplate-unsigned-destroy/<int:pk>/',PdfFileTemplateUnsignedDestroyApiView.as_view()),
    path('partyuser/typeletter/pdffiletemplate-signed-update/',PdfFileTemplateSignedUpdateApiView.as_view()),
]

