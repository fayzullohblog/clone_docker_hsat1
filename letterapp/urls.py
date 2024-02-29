from django.urls import path
from .views import (
        ZarikCreateApiView,
        PdfFileTemplateView,
        RecentlyCreatedPdf,
        NotificationListApiView,
)

urlpatterns =  [
    path('get_inn/',PdfFileTemplateView.as_view()),
    path('zarik-create/',ZarikCreateApiView.as_view()),
    path('get_inn/recentlycreatedpdf/',RecentlyCreatedPdf.as_view()),
    path('notification/',NotificationListApiView.as_view()),
   
]









