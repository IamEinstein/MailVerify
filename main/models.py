from django.db import models

# Create your models here.


class Id(models.Model):
    unique_id = models.CharField(max_length=100)
    time_created = models.DateTimeField()
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=30)
    mail = models.CharField(max_length=100)
    mail_is_real = models.BooleanField(default=False, blank=False)


class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=30)
    mail = models.CharField(max_length=100)
