from django.shortcuts import render
from django.http import HttpResponseRedirect
from api.models import ShortUrls
from api.helper import add_new_url
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.


def home(request):
    base_context = {
        "title": "This is title",
        "icon": "success",
        "text": "",
        "showAlert": False
    }
    if request.GET.get('isRedirected', False):
        base_context["icon"] = "error"
        base_context["title"] = "You entered an invalid url!"
        base_context["showAlert"] = True
    if request.method == 'POST':
        # Save the submitted data
        url = request.POST.get("url")
        short = request.POST.get("short_name")
        print(request.POST)
        base_context['showAlert'] = True
        try:
            new_url = add_new_url(url, short)
            short_url = "{}/{}".format(get_current_site(request).domain, new_url)
            base_context["text"] = "Goto {}".format(short_url)
            base_context["title"] = "Short URL added successfully!"
            base_context["icon"] = "success"
        except:
            base_context["icon"] = "error"
            base_context["title"] = "Unable to create a short URL for the supplied data!"

    return render(request, "api/home.html", base_context)


def redirect(request, short=None):
    try:
        redirect_url = ShortUrls.objects.get(short_name=short).url
    except ObjectDoesNotExist:
        redirect_url = "/?isRedirected=True"
    return HttpResponseRedirect(redirect_url)
