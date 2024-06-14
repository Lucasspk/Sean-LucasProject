from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, default='null', null=True, blank=True)
    image2 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, default='null', null=True, blank=True)
    image3 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, default='null', null=True, blank=True)
    image4 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, default='null', null=True, blank=True)
    created_at = models.DateTimeField(default= datetime.now, blank= True)
    link = models.URLField(max_length=4000, default=None, blank=True)
    linkDescription = models.CharField(max_length=4000, default=None, blank=True)