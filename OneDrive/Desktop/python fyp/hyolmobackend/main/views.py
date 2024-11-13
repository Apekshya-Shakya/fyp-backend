from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .models import *

class EventDetail(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = Eventserializer

class MemberDetail(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = Memberserializer

class IntroductionDetail(ModelViewSet):
    queryset = Introduction.objects.all()
    serializer_class = Introductionserializer

class MessagefromPresidentandGeneralSecretaryDetail(ModelViewSet):
    queryset = MessagefromPresidentandGeneralSecretary.objects.all()
    serializer_class = MessagefromPresidentandGeneralSecretaryserializer

class ActivitiesDetail(ModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = Activitiesserializer

class NewsDetail(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = Newsserializer

class ImageMediaDetail(ModelViewSet):
    queryset = ImageMedia.objects.all()
    serializer_class = ImageMediaserializer

class VideoMediaDetail(ModelViewSet):
    queryset = VideoMedia.objects.all()
    serializer_class = VideoMediaserializer

class ContactUsDetail(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsserializer