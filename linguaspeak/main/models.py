from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class LinguaLevel(models.Model):
    title = models.CharField(max_length=100)
    short_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Language(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Thread(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    lingualevel = models.ForeignKey(LinguaLevel, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    max_people = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main-home')
