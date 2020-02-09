from django.test import TestCase
from api.helper import add_new_url
from api.models import ShortUrls

# Create your tests here.
class ShortURLTest(TestCase):
    def test_create_link(self):
        # Test creation without short name
        new_short = add_new_url("https://www.google.com")
        self.assertEqual(ShortUrls.objects.filter(short_name=new_short).count(), 1)
        # Test with custom short name
        add_new_url("https://www.google.com", "abc")
        self.assertEqual(ShortUrls.objects.filter(short_name="abc").count(), 1)