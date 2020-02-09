from django.db import models
from django.core.validators import URLValidator


# Create your models here.
class ShortUrls(models.Model):
    short_name = models.CharField(max_length=10)
    url = models.TextField(validators=[URLValidator()])
