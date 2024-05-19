from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
import schwa_app.views as schwa_views


class SchwaHome(TestCase):
    def setUp(self):

        self.email = 'dave@dave.com'
        self.password = 'davedavedave'
        self.first_name = 'dave'
        self.last_name = 'dave'
        User.objects.create_user(email=self.email, username=self.email, password=self.password, first_name=self.first_name,
                                 last_name=self.last_name)

    def test_unauthenticate_user_reroutes_home(self):
        client = Client()
        client.logout()
        response = client.get('/schwa/')

        self.assertEqual('/', response.url)

    def test_authenticated_user_can_access(self):
        client = Client()
        client.login(username=self.email, password=self.password)
        response = client.get('/schwa/')

        self.assertEqual(response.resolver_match.func, schwa_views.schwa_home)

