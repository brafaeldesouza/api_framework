import json
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth.models import User

class LoggedInTestCaseMixin(TestCase):
    """Test class to authenticate the test user

    Args:
        TestCase (Class): Default class for test cases
    """
    def setUp(self):
        self.client = APIClient()
        self.user_logged_in = User(username='admin')
        self.user_logged_in.set_password('123456')
        self.user_logged_in.save()

        token = Token.objects.get_or_create(user=self.user_logged_in)

        self.client.force_authenticate(user=self.user_logged_in, token=token[0].key)