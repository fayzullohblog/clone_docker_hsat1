from django.urls import path
from .views import LetterTemplatesCreateApiView

urlpatterns = [
    path('create-letter/',LetterTemplatesCreateApiView.as_view())
]