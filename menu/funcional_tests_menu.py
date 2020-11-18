from selenium import webdriver
from selenium.webdriver import Firefox
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from search_and_sub.models import Product
import os
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class MenuFonctionalTests(StaticLiveServerTestCase):
    """
    3 functionals tests are done in this class.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        PATH = "/usr/local/bin/geckodriver"
        firefox_options = webdriver.FirefoxOptions()
        # firefox_options.headless = True
        firefox_options.add_argument('--window-size=1920x1080')
        cls.selenium = Firefox(executable_path=PATH, options=firefox_options)

    def test_login(self):
        """
        This test will check if a user can login after an account creation.
        """
        self.product_tested = Product(
        #product creation in the table "Product" in the data base
            id = 12124,
            p_code = '3083680484466',
            p_name = 'Taboulé oriental',
            p_nutrition_grade_fr = 'b',
            p_categories_tags = 'starters',
            p_image_url = 'https://static.openfoodfacts.org/images/products/308/368/048/4466/front_fr.70.400.jpg'
            )
        self.product_tested.save()
        self.product_tested = Product(
        #product creation in the table "Product" in the data base
            id = 12095,
            p_code = '20023959',
            p_name = 'Saucisses aux lentilles',
            p_nutrition_grade_fr = 'a',
            p_categories_tags = 'meals',
            p_image_url = 'https://static.openfoodfacts.org/images/products/20023959/front_fr.20.400.jpg'
            )
        self.product_tested.save()
        self.product_tested = Product(
        #product creation in the table "Product" in the data base
            id = 18326,
            p_code = '3021761202974',
            p_name = 'Pom Potes 5 fruits',
            p_nutrition_grade_fr = 'a',
            p_categories_tags = 'desserts',
            p_image_url = 'https://static.openfoodfacts.org/images/products/302/176/120/2974/front_fr.6.400.jpg'
            )

        self.product_tested.save()
        self.server = self.live_server_url+"/user/register/"
        self.selenium.get(self.server)
        self.username = self.selenium.find_element_by_name("username")
        self.password1 = self.selenium.find_element_by_name("password1")
        self.password2 = self.selenium.find_element_by_name("password2")
        self.creation_button = self.selenium.find_element_by_id("creation_btn")
        self.username.send_keys("Marcel")
        self.password1.send_keys("wxcvbn1234")
        self.password2.send_keys("wxcvbn1234")
        self.creation_button.submit()
        time.sleep(1)
        #login with the user name and password created above
        self.server = self.live_server_url+"/user/login/"
        self.selenium.get(self.server)
        self.username = self.selenium.find_element_by_name("username")
        self.password1 = self.selenium.find_element_by_name("password")
        self.login_button = self.selenium.find_element_by_id("login_btn")
        self.username.send_keys("Marcel")
        self.password1.send_keys("wxcvbn1234")
        self.login_button.click()
        self.conf_connex = WebDriverWait(self.selenium, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "welcome_msg")))
        time.sleep(1)
        self.assertEqual(self.conf_connex.text, "Bonjour Marcel")

        self.server = self.live_server_url+"/menu/menu_generation/"
        # self.selenium = get(self.server)
        self.link = self.selenium.find_element_by_id("icon_menu")
        self.link.click()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
