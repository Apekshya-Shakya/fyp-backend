from rest_framework import serializers
from .models import *

class Eventserializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class Memberserializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class Introductionserializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'

class MessagefromPresidentandGeneralSecretaryserializer(serializers.ModelSerializer):
    class Meta:
        model = MessagefromPresidentandGeneralSecretary
        fields = '__all__'
    
class Activitiesserializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'

class Newsserializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class ImageMediaserializer(serializers.ModelSerializer):
    class Meta:
        model = ImageMedia
        fields = '__all__'

class VideoMediaserializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMedia
        fields = '__all__'
        
class ContactUsserializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'