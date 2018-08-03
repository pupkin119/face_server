from django.db import models

# Create your models here.

class WriteErrorToDb(models.Model):
    module = models.CharField(max_length = 40)
    client_id = models.UUIDField(max_length = 40)
    error_id = models.IntegerField()