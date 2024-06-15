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


    def test_access_schwa(self):
        self.login()
        time.sleep(.5)
        self.driver.get(f'{self.live_server_url}/profile/')

        time.sleep(.5)
        icon = self.driver.find_element(By.ID, 'schwa_icon')
        icon.click()
        time.sleep(.5)
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}/language_academy/')

    def test_pyrismus_navs_back(self):
        self.login()
        time.sleep(.5)
        self.driver.get(f'{self.live_server_url}/language_academy/')
        time.sleep(.5)
        self.driver.find_element(By.ID, 'pyrismus_icon').click()
        time.sleep(.5)
        self.assertEqual(self.driver.current_url, f'{self.live_server_url}/profile/')
