from django.db import models

# Create your models here.

class ContactForm(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=1000)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
