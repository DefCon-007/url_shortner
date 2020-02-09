import string
import random
from api.models import ShortUrls
from django.core.exceptions import ValidationError
from api.exceptions import InvalidURLException
from django.conf import settings


def get_random_string(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def add_new_url(url, short_name=None):
    if not short_name:
        short_name = get_random_string()
    instance = ShortUrls(
        url=url,
        short_name=short_name
    )
    try:
        instance.full_clean()
        instance.save()
    except ValidationError:
        raise InvalidURLException
    return short_name


def add_list_of_urls(url_list):
    """

    :param url_list: List of tuple, 1st - url 2nd(optional) - shortname
    :return: List of shortnames
    """
    query_set = [ShortUrls(url=tup[0], short_name=tup[1] if tup[1] else get_random_string()) for tup in url_list]

    return ["http://{}/{}".format(settings.BASE_URL,d.short_name) for d in ShortUrls.objects.bulk_create(query_set)]
