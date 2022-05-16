import json
from django.shortcuts import resolve_url as r
from django.urls import reverse

from api.tests.base import LoggedInTestCaseMixin

class RegisterAPIViewTest(LoggedInTestCaseMixin):
    def setUp(self):
        super(RegisterAPIViewTest, self).setUp()

    def test_get_registers(self):

        response = self.client.get(reverse('api:list_register', kwargs={}), format="json")
        data     = json.loads(response.content)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['data'][0]['title'], "delectus aut autem")
        self.assertEqual(data['data'][3]['title'], "et porro tempora")
        
        