from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote_code = models.CharField(max_length=200)
    metadata_text = models.CharField(max_length=200)
    quote_type = models.IntegerField(default=0)
    quote_amount = models.FloatField(default=0.0)