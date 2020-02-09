from django.shortcuts import render
from api.helper import get_random_string
# Create your views here.

def home(request):
    return 123


def redirect(request, short=None):
    print(short)
