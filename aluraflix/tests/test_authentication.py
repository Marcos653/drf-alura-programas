from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')

    
    def test_authentication(self):
        """Teste que verifica authentication"""
        user =authenticate(username='c3po', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    
    def test_request_get_not_auth(self):
        """Teste que verifica uma request GET sem auth"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_auth_user_with_wrong_username(self):
        """Test verific auth wrong user name"""
        user =authenticate(username='c3po', password='12345')
        self.assertFalse((user is not None) and user.is_authenticated)


    def test_request_get_with_user_auth(self):
        """Test q verifica uma request GET authentication"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
