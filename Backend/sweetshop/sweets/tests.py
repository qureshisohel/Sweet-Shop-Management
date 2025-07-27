from django.test import TestCase
from .models import Sweet
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class SweetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='pass')
        self.client.force_authenticate(user=self.user)
        self.sweet = Sweet.objects.create(name="Ladoo", category="Indian", price=10.0, quantity=5)

    def test_purchase(self):
        response = self.client.post(f'/api/sweets/{self.sweet.id}/purchase/')
        self.assertEqual(response.status_code, 200)
        self.sweet.refresh_from_db()
        self.assertEqual(self.sweet.quantity, 4)
