from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class App(models.Model):
    app_character = models.CharField('Character', max_length=100,blank=True)
    app_integer = models.IntegerField('Integer', default=1,blank=True)
    app_float = models.FloatField('Float',default=0.5,blank=True)
    app_boolean = models.BooleanField('Boolean', default=False,blank=True)
    app_date = models.DateField('Date', default=datetime.date.today, blank=True)
    app_date_time = models.DateTimeField('DateTime', default=timezone.now())

class App2(models.Model):
    app_character = models.CharField('Character', max_length=100,blank=True)
    app_integer = models.IntegerField('Integer', default=1,blank=True)
    app_float = models.FloatField('Float',default=0.5,blank=True)
    app_boolean = models.BooleanField('Boolean', default=False,blank=True)
    app_date = models.DateField('Date', default=datetime.date.today, blank=True)
    app_date_time = models.DateTimeField('DateTime', default=timezone.now())

class App3(models.Model):
    app_character = models.CharField('Character', max_length=100,blank=True)
    app_integer = models.IntegerField('Integer', default=1,blank=True)
    app_float = models.FloatField('Float',default=0.5,blank=True)
    app_boolean = models.BooleanField('Boolean', default=False,blank=True)
    app_date = models.DateField('Date', default=datetime.date.today, blank=True)
    app_date_time = models.DateTimeField('DateTime', default=timezone.now())

