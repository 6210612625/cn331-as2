
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.

class UserViewTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='user1', password='', email='user1@example.com')

    def test_index_view_with_authenciation(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_without_authenciation(self):
        c = Client()
        user = User.objects.get(username='user1')
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 302)
        
    def test_login_view_unsuccessful(self):
        c = Client()
        user = User.objects.get(username='user1')
        response = c.post(reverse('users:login'), {'username': 'user1', 'password': ''})        
        self.assertEqual(response.status_code, 200)
