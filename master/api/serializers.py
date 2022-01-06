from rest_framework import serializers
from master.models import ContactUs



class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['name', 'subject', 'email', 'message', ]