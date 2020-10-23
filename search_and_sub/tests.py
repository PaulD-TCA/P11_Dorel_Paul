from django.urls import reverse, resolve
from django.test import TestCase, Client
from search_and_sub.models import Product, Backup
from django.contrib.auth.models import User
from search_and_sub.views import my_favourites, results, home


# Create your tests here.
class PageProjectTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_results_page(self):
        response = self.client.get(reverse('results_page'))
        self.assertEqual(response.status_code, 200)

    def test_my_favourites_page(self):
        response = self.client.get(reverse('my_favourites_page'))
        self.assertEqual(response.status_code, 200)


class ModelsTestCase(TestCase):
    def setUp(self):
        self.product_tested = Product(
            id = 8000,
            p_code = '3270160860487',
            p_name = 'Colombo de poissons, riz et lentilles corail - Picard - 300 g e',
            p_nutrition_grade_fr = 'a',
            p_categories_tags = 'Plats à base de riz',
            p_url = 'https://fr.openfoodfacts.org/produit/3270160860487/colombo-de-poissons-riz-et-lentilles-corail-picard',
            p_image_url = 'https://static.openfoodfacts.org/images/products/327/016/086/0487/nutrition_fr.34.400.jpg',
            p_fat = '5.7',
            p_salt = '1.7',
            p_sugars = '1',
            p_saturated_fat = '0.54'
            )
        self.product_tested.save()

        self.user_tested = User(
            id = 80,
            username="Armelle",
            password="password1234"
            )
        self.user_tested.save()

        self.backup_tested = Backup(
            id = 1,
            p_id_id = 8000,
            u_id_id = 80
            )
        self.backup_tested.save()


    def test_create_product(self):
        self.assertEqual(self.product_tested.id, 8000)
        self.assertEqual(self.product_tested.p_code, '3270160860487')
        self.assertEqual(self.product_tested.p_name, 'Colombo de poissons, riz et lentilles corail - Picard - 300 g e')
        self.assertEqual(self.product_tested.p_nutrition_grade_fr, 'a')
        self.assertEqual(self.product_tested.p_categories_tags, 'Plats à base de riz')
        self.assertEqual(self.product_tested.p_url, 'https://fr.openfoodfacts.org/produit/3270160860487/colombo-de-poissons-riz-et-lentilles-corail-picard')
        self.assertEqual(self.product_tested.p_image_url, 'https://static.openfoodfacts.org/images/products/327/016/086/0487/nutrition_fr.34.400.jpg')
        self.assertEqual(self.product_tested.p_fat, '5.7')
        self.assertEqual(self.product_tested.p_salt, '1.7')
        self.assertEqual(self.product_tested.p_sugars, '1')
        self.assertEqual(self.product_tested.p_saturated_fat, '0.54')

    def test_create_user(self):
        self.assertEqual(self.user_tested.username, "Armelle")
        self.assertEqual(self.user_tested.password, "password1234")

    def test_create_backup(self):
        self.assertEqual(self.backup_tested.id, 1)
        self.assertEqual(self.backup_tested.p_id_id, 8000)
        self.assertEqual(self.backup_tested.u_id_id, 80)

class UrlsTestCase(TestCase):
    def test_my_favourites_url(self):
        url = reverse('my_favourites_page')
        self.assertEqual(resolve(url).func, my_favourites)

    def test_my_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_my_results_url(self):
        url = reverse('results_page')
        self.assertEqual(resolve(url).func, results)
