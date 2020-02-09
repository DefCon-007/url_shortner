from django.db import models
from django.core.validators import URLValidator
from django import forms


# Create your models here.
class ShortUrls(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    url = models.TextField(validators=[URLValidator()])


class UrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrls
        fields = ['url', 'short_name']

