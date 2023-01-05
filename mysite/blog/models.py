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

class Voetbalspeler(models.Model):
   naam_van_de_voetballer = models.CharField(max_length=200)
   actuele_voetbalclub = models.CharField(max_length=200)
   naam_van_de_auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   datum_van_invoer = models.DateTimeField(default=timezone.now)
   datum_van_laatste_aanpassing = models.DateTimeField(blank=True, null=True)

   def publish(self):
       self.published_date = timezone.now()
       self.save()

   def __str__(self):
       return self.naam_van_de_voetballer