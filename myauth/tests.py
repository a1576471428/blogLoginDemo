from django.test import Client, RequestFactory, TestCase

# Create your tests here.
from django.urls import reverse

from myauth.models import BlogUser


class AuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_register(self):
        self.assertEquals(0, len(BlogUser.objects.filter(email='user123@user.com')))
        response = self.client.post(reverse('myauth:register'), {
            'username': 'user1233',
            'email': 'user123@user.com',
            'password1': 'password123',
            'password2': 'password123',
            'phone':'13333333333',
        })
        self.assertEqual(1, len(BlogUser.objects.filter(email='user123@user.com')))
