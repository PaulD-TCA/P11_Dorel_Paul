from django.urls import reverse
from django.test import TestCase, Client

from django.contrib.auth.models import User


class LoginPageTestCase(TestCase):
    def test_login_page(self):
        response = self.client.get(reverse('login_page'))
        self.assertEqual(response.status_code, 200)
