from django.shortcuts import render
from django.http import HttpResponseRedirect
from api.models import ShortUrls, UrlForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.shortcuts import get_current_site
from api.helper import get_random_string
# Create your views here.


def home(request):
    base_context = {
        "title": "This is title",
        "icon": "success",
        "text": "",
        "showAlert": False
    }
    if request.method == 'POST':
        # Save the submitted data
        base_context['showAlert'] = True
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            base_context["icon"] = "success"
            base_context["title"] = "Short URL added successfully!"
            base_context["text"] = "Goto {}/{}".format(get_current_site(request).domain, form.cleaned_data.get('short_name', None))
        else:
            base_context["icon"] = "error"
            base_context["title"] = "Unable to create a short URL for the supplied data!"
    else:
        form = UrlForm()
    base_context["form"] = form
    return render(request, "api/home.html", base_context)


def redirect(request, short=None):
    try:
        redirect_url = ShortUrls.objects.get(short_name=short).url
    except ObjectDoesNotExist:
        redirect_url = "/"
    print(redirect_url)
    return HttpResponseRedirect(redirect_url)
