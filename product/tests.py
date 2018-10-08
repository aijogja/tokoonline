from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your tests here.

class TokenTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="aijogja", password="zxcvbnm,")

    def test_token_on_user_created(self):
        user = User.objects.get(username="aijogja")
        self.assertIsNotNone(user.auth_token)
