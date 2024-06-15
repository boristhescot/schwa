from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.test import Client

import schwa_app.views as schwa_views
import userhome.views as userhome_views


class SchwaTestCase(TestCase):

    def setUp(self) -> None:
        self.email = 'dave@dave.com'
        self.password = 'davedavedave'
        self.first_name = 'dave'
        self.last_name = 'dave'
        User.objects.create_user(email=self.email, username=self.email, password=self.password, first_name=self.first_name,
                                 last_name=self.last_name)

    def test_access(self):
        client = Client()
        client.login(username=self.email, password=self.password)
        response = client.get('/language_academy/')
        self.assertEqual(response.resolver_match.func, schwa_views.schwa_home)