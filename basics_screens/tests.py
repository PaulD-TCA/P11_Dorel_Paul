from django.urls import reverse
from django.test import TestCase, Client

# Create your tests here.
class LegalNoticeTestCase(TestCase):
    def test_mentions_legale_found(self):
        response = self.client.get(reverse('legal_notice_page'))
        self.assertEqual(response.status_code, 200)
