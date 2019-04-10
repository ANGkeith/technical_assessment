from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import LanguageLabel, LanguageData

from rest_framework.authtoken.models import Token


class ApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create(username='admin')
        user.set_password('admin')
        user.save()
        self.user = User.objects.get(username='admin')

        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION ='Token ' + token.key)

        # Mock data
        LanguageLabel.objects.create(shortName='lb')


    def test_api_token_auth(self):
        response = self.client.post('/api-token-auth/', {'username': 'admin', 'password':'admin'},format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_language_labels(self):
        response = self.client.post('/api/language-labels/', {'shortName': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_language_labels(self):
        response = self.client.get('/api/language-labels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_single_language_labels(self):
        response = self.client.get('/api/language-labels/lb/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)







