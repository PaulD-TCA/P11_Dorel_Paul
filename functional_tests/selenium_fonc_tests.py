from selenium import webdriver
from selenium.webdriver import Firefox
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from search_and_sub.models import Product
import os

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class MySeleniumTests(StaticLiveServerTestCase):
    """
    3 functionals tests are done in this class.
    """
    #chrome driver
    # @classmethod
    # def setUpClass(cls):
    #     super().setUpClass()
    #     path_to_folder = os.path.abspath("")
    #     PATH = path_to_folder+"/functional_tests/chromedriver"
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--headless')
    #     chrome_options.add_argument('--disable-gpu')
    #     chrome_options.add_argument('--remote-debugging-port=9222')
    #     chrome_options.add_argument('--window-size=1920x1080')
    #     cls.selenium = webdriver.Chrome(PATH, options=chrome_options)

    #firefox
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # path_to_folder = os.path.abspath("")
        # PATH = path_to_folder+"/functional_tests/geckodriver"
        PATH = "/usr/local/bin/geckodriver"
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True
        firefox_options.add_argument('--window-size=1920x1080')
        cls.selenium = Firefox(executable_path=PATH, options=firefox_options)

    def test_search(self):
        """
        We are testing if a product is returned when we are looking for that
        in the search menu.
        """
        self.product_tested = Product(
        #product creation in the table "Product" in the data base
            id = 8000,
            p_code = '3270160860487',
            p_name = 'Colombo de poissons, riz et lentilles corail',
            p_nutrition_grade_fr = 'a'
            )
        self.product_tested.save()
        #The name of the searched product have to be returned in this test
        self.server = self.live_server_url
        self.selenium.get(self.server)
        self.search = self.selenium.find_element_by_id("form-lg")
        self.search.send_keys("poisson")
        self.search.send_keys(Keys.RETURN)
        self.searched_value = WebDriverWait(self.selenium, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "card-title"))
            )
        self.assertEqual(
            self.searched_value.text, "Colombo de poissons, riz et lentilles corail")

    def test_a_register(self):
        """
        This test will check if a new user can be created.
        """
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
        self.confirmation = WebDriverWait(self.selenium, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "messages")))
        self.assertEqual(self.confirmation.text, "Le compte à été créé pourMarcel")

    def test_login(self):
        """
        This test will check if a user can login after an account creation.
        """
        # User creation with Selenium
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
        #login with the user name and password created above
        self.server = self.live_server_url+"/user/login/"
        self.selenium.get(self.server)
        self.username = self.selenium.find_element_by_name("username")
        self.password1 = self.selenium.find_element_by_name("password")
        self.login_button = self.selenium.find_element_by_id("login_btn")
        self.username.send_keys("Marcel")
        self.password1.send_keys("wxcvbn1234")
        self.login_button.click()
        # self.conf_connex = WebDriverWait(self.selenium, 10).until(
        #     expected_conditions.presence_of_element_located((By.ID, "welcome_msg")))
        # self.assertEqual(self.conf_connex.text, "Bonjour Marcel")

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
