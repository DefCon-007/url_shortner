from django.shortcuts import render
from django.http import HttpResponseRedirect
from api.models import ShortUrls, UrlForm
from django.core.exceptions import ObjectDoesNotExist

from api.helper import get_random_string
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UrlForm()
    return render(request, "api/home.html", {'form': form})


def redirect(request, short=None):

    try:
        redirect_url = ShortUrls.objects.get(short_name=short).url
    except ObjectDoesNotExist:
        redirect_url = "/"
    print(redirect_url)
    return HttpResponseRedirect(redirect_url)
