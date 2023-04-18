from rest_framework import serializers
from .models import Phone, Notebook

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['name', 'price']



class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ['name', 'price']