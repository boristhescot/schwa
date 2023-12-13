from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.test import Client
import main.views as main_views
import userhome.views as userhome_views


class AuthTestCase(TestCase):

    def setUp(self) -> None:
        self.email = 'dave@dave.com'
        self.password = 'davedavedave'
        self.first_name = 'dave'
        self.last_name = 'dave'
        User.objects.create_user(email=self.email, username=self.email, password=self.password, first_name=self.first_name,
                                 last_name=self.last_name)



    def test_logged_out_user_gets_login_screen(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.resolver_match.func, main_views.main_view)


    def test_logged_in_user_gets_profile_screen(self):
        client = Client()
        client.login(username=self.email, password=self.password)
        response = client.get('/')
        self.assertEqual(response.url, '/profile/')


    def test_logged_out_user_cant_access_profile(self):
        client = Client()
        client.logout()
        response = client.get('/profile/')
        self.assertEqual(response.url, '/')


    def test_creating_an_existing_user_shows_msg(self):
        client = Client()
        response = client.post('/user_auth/register_user',
                               {'email': self.email,
                                'username': self.email,
                                'password': self.password,
                                'first_name': self.first_name,
                                'last_name': self.last_name}, follow=True)

        self.assertInHTML('Account with email already exists', response.content.decode())
