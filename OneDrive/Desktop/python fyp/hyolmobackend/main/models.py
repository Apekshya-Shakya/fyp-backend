from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Event(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    

class Member(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField()
    designation = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    membertype= models.CharField(max_length=50)
    
class Introduction(models.Model):
    text= models.CharField(max_length=500)
    title= models.CharField(max_length=500)

class MessagefromPresidentandGeneralSecretary(models.Model):
    text= models.CharField(max_length=500)
    photo = models.ImageField()
    name= models.CharField(max_length=50)
    designation= models.CharField(max_length=50)
    

class Activities(models.Model):
    description= models.CharField(max_length=500)
    photo = models.ImageField()
    name= models.CharField(max_length=50)
    eventtype= models.CharField(max_length=50)
    date = models.DateTimeField()
    

class News(models.Model):
    text= models.CharField(max_length=500)
    photo = models.ImageField()
    name= models.CharField(max_length=50)
    newstype= models.CharField(max_length=50)
    
class ImageMedia(models.Model):
    text= models.CharField(max_length=500) 
    photo = models.ImageField()
    name= models.CharField(max_length=50)
    
class VideoMedia(models.Model):
    text= models.CharField(max_length=500) 
    video = models.FileField()
    name= models.CharField(max_length=50)
    
class ContactUs(models.Model):
    message= models.CharField(max_length=500) 
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    location= models.CharField(max_length=50)

