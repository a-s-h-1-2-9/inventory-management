# inventory/tests.py
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import InventoryItem

class UserRegistrationTests(APITestCase):
    def test_user_registration(self):
        url = '/api/adminuser/register/'
        data = {
            "username": "testuser",
            "password": "testpass123",
            "email": "test@example.com"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class InventoryItemTests(APITestCase):
    def setUp(self):
        # Register a user
        url = '/api/adminuser/register/'
        data = {
            "username": "testuser",
            "password": "testpass123",
            "email": "test@example.com"
        }
        self.client.post(url, data)

        # Obtain token
        token_url = '/api/adminuser/logintoken/'
        token_data = {
            "username": "testuser",
            "password": "testpass123"
        }
        token_response = self.client.post(token_url, token_data)
        self.token = token_response.data['access']
        
        # Set authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Create an inventory item
        self.item = InventoryItem.objects.create(name='Test Item', quantity=10)

    def test_create_item(self):
        url = '/api/inventory-items/'
        data = {'name': 'New Item', 'quantity': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_item(self):
        url = f'/api/inventory-items/{self.item.id}/'
        data = {'name': 'Updated Item', 'quantity': 20}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        url = f'/api/inventory-items/{self.item.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
