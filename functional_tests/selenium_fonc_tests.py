from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from search_and_sub.models import Product
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
import os


class MySeleniumTests(StaticLiveServerTestCase):
    """
    3 functionals tests are done in this class.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.pathtofolder = os.path.abspath("")
        # cls.link = "functional_tests/chromedriver"
        cls.selenium = webdriver.Chrome(executable_path=r"functional_tests/chromedriver")
        # os.environ["webdriver.chrome.driver"] = cls.link
        # cls.selenium = webdriver.Chrome(cls.link)

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")

        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-setuid-sandbox")


        cls.selenium = webdriver.Chrome(executable_path=r"functional_tests/chromedriver", options=chromeOptions)

        # cls.selenium = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # cls.selenium = webdriver.Chrome(executable_path=ChromeDriverManager().get_download_path(version="86.0.4240.22"))
        # cls.st = os.stat(cls.chrome_driver_path)
        # os.chmod(self.chrome_driver_path, cls.st.st_mode | stat.S_IEXEC)

        # cls.PATH_AND_AUTH = os.chmod(cls.PATH, 755)
        # print(type(cls.PATH_AND_AUTH))
        # cls.PATH = os.chmod(os.path.join(cls.pathtofolder, "functional_tests/chromedriver"), 0o755)
        # print(cls.PATH)
        # cls.selenium = webdriver.Chrome(os.chmod("functional_tests/chromedriver", int("0755")))
        cls.selenium.implicitly_wait(10)

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
        self.confirmation = self.selenium.find_element_by_id("messages")
        self.assertEqual(self.confirmation.text, "Le compte à été créé pourMarcel")

    # def test_login(self):
    #     """
    #     This test will check if a user can login after an account creation.
    #     """
    #     # User creation with Selenium
    #     self.server = self.live_server_url+"/user/register/"
    #     self.selenium.get(self.server)
    #     self.username = self.selenium.find_element_by_name("username")
    #     self.password1 = self.selenium.find_element_by_name("password1")
    #     self.password2 = self.selenium.find_element_by_name("password2")
    #     self.creation_button = self.selenium.find_element_by_id("creation_btn")
    #     self.username.send_keys("Marcel")
    #     self.password1.send_keys("wxcvbn1234")
    #     self.password2.send_keys("wxcvbn1234")
    #     self.creation_button.submit()
    #     #login with the user name and password created above
    #     self.server = self.live_server_url+"/user/login/"
    #     self.selenium.get(self.server)
    #     self.username = self.selenium.find_element_by_name("username")
    #     self.password1 = self.selenium.find_element_by_name("password")
    #     self.login_button = self.selenium.find_element_by_id("login_btn")
    #     self.username.send_keys("Marcel")
    #     self.password1.send_keys("wxcvbn1234")
    #     self.login_button.click()
    #     self.conf_connex = WebDriverWait(self.selenium, 10).until(
    #         expected_conditions.presence_of_element_located((By.ID, "welcome_msg")))
    #     self.assertEqual(self.conf_connex.text, "Bonjour Marcel")

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
