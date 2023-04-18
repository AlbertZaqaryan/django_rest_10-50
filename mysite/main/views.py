from django.shortcuts import render
from .models import Phone, Notebook
from .serializers import PhoneSerializer, NotebookSerializer
from rest_framework import viewsets
# Create your views here.

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer



class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer