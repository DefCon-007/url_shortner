from django.shortcuts import render

# Create your views here.

def home(request):
    return 123


def redirect(request, short=None):
    print(short)
