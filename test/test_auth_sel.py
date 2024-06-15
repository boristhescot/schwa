import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from django.contrib.auth.models import User

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.webdriver import WebDriver



class LoginInTest(StaticLiveServerTestCase):
    email = 'dave@dave.com'
    password = 'davedavedave'
    first_name = 'dave'
    last_name = 'dave'
    @classmethod
    def setUpClass(cls):

        super().setUpClass()
        cls.driver = WebDriver()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def create_user(self):
        User.objects.create_user(email=self.email, username=self.email, password=self.password,
                                 first_name=self.first_name,
                                 last_name=self.last_name)

    def login(self):
        self.create_user()
        self.driver.get(f'{self.live_server_url}')
        username = self.driver.find_element(By.ID, "username")
        username.send_keys(self.email)
        pw = self.driver.find_element(By.ID, 'password')
        pw.send_keys(self.password)
        pw.send_keys(Keys.ENTER)

    def print_source(self):
        elem = self.driver.find_element("xpath", "//*")
        source_code = elem.get_attribute("outerHTML")
        print(source_code)
    def test_load(self):
        self.driver.get(f'{self.live_server_url}')
        print(self.driver.title)
        self.assertEqual(self.driver.title, 'Pyrismus')

    def test_create_new_user(self):

        self.driver.get(f'{self.live_server_url}')
        time.sleep(.5)
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()
        time.sleep(.5)
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}/user_auth/new_user/')
        self.driver.find_element(By.ID, "first_name").send_keys(self.first_name)
        self.driver.find_element(By.ID, "last_name").send_keys(self.last_name)
        self.driver.find_element(By.ID, "username").send_keys(self.email)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.ID, "register").click()
        time.sleep(.5)
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}/')

    def test_login(self):

        self.login()
        time.sleep(.5)
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}/profile/')

