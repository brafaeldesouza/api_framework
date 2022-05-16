import json
from django.test import TestCase
from model_mommy import mommy
from api.models import Log

class LogModelTest(TestCase):
    def setUp(self):
        self.graph = mommy.make(Log)
    
    def test_model_exists(self):
        self.assertTrue(Log.objects.exists())
