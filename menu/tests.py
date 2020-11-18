from django.test import TestCase, Client
from django.urls import reverse, resolve
from menu.views import menu_generation
from search_and_sub.models import Product

# Create your tests here.
# class PageMenuTestCase(TestCase):
#     def test_menu_page(self):
#         response = self.client.get(reverse('menu_generation'))
#         self.assertEqual(response.status_code, 200)

class UrlsMenuTestCase(TestCase):
    def test_Menu_url(self):
        url = reverse('menu_generation')
        self.assertEqual(resolve(url).func, menu_generation)
