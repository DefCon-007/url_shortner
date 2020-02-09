import string
import random
from api.models import ShortUrls
from django.core.exceptions import ValidationError
from api.exceptions import InvalidURLException


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
