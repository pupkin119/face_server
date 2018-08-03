from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Clients(models.Model):
    client_id = models.UUIDField(max_length=40)
    restaurant_id = models.UUIDField(max_length=40)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

class Client_imgs(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    encoded_image = models.CharField(max_length=245000)


