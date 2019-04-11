from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import LanguageLabel, LanguageData, DoctypeData, DoctypeLabel, ConfidentialityData, ConfidentialityLabel

from rest_framework.authtoken.models import Token


class ApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # mock user creation
        user = User.objects.create(username='admin')
        user.set_password('admin')
        user.save()
        self.user = User.objects.get(username='admin')

        # generate user token
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION ='Token ' + token.key)

        # mock data
        LanguageLabel.objects.create(shortName='lb', name='label')
        LanguageLabel.objects.create(shortName='lb2', name='label2')
        language_label = LanguageLabel.objects.get(shortName='lb')
        LanguageData.objects.create(language_label=language_label, total_docs=3)

        DoctypeLabel.objects.create(name='testname')
        DoctypeData.objects.create(name='testname', total_docs='0')

        ConfidentialityLabel.objects.create(name='testname')
        ConfidentialityData.objects.create(name='testname', total_docs='0')






    def test_api_token_auth(self):
        response = self.client.post('/api-token-auth/', {'username': 'admin', 'password':'admin'},format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # LANGUAGE
    def test_create_language_labels(self):
        response = self.client.post('/api/language-labels/', {'shortName': 't', 'name': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_language_labels(self):
        response = self.client.get('/api/language-labels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_single_language_labels(self):
        response = self.client.put('/api/language-labels/lb/', {'shortName': 'lb', 'name': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_single_language_labels(self):
        response = self.client.get('/api/language-labels/lb/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_single_language_labels(self):
        response = self.client.delete('/api/language-labels/lb/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_language_datas(self):
        response = self.client.post('/api/language-datas/', {'short_name': 'lb2', 'total_docs': 3}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_language_datas(self):
        response = self.client.get('/api/language-datas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_single_language_datas(self):
        response = self.client.put('/api/language-datas/lb/', {'short_name': 'lb', 'total_docs': 4}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_single_language_datas(self):
        response = self.client.get('/api/language-datas/lb/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_single_language_datas(self):
        response = self.client.delete('/api/language-datas/lb/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    # Doctype
    def test_create_doctype_labels(self):
        response = self.client.post('/api/doctype-labels/', {'name': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_doctype_labels(self):
        response = self.client.get('/api/doctype-labels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_single_doctype_labels(self):
        response = self.client.put('/api/doctype-labels/testname/', {'name': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_single_doctype_labels(self):
        response = self.client.get('/api/doctype-labels/testname/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_single_doctype_labels(self):
        response = self.client.delete('/api/doctype-labels/testname/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_doctype_datas(self):
        response = self.client.post('/api/doctype-datas/', {'name': 'testname2', 'total_docs': 3}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_doctype_datas(self):
        response = self.client.get('/api/doctype-datas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_single_doctype_datas(self):
        response = self.client.put('/api/doctype-datas/testname/', {'name': 'testname2', 'total_docs': 4}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_single_doctype_datas(self):
        response = self.client.get('/api/doctype-datas/testname/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_single_doctype_datas(self):
        response = self.client.delete('/api/doctype-datas/testname/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    # Confidentiality
    def test_create_confidentiality_labels(self):
        response = self.client.post('/api/confidentiality-labels/', {'name': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_confidentiality_labels(self):
        response = self.client.get('/api/confidentiality-labels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_single_confidentiality_labels(self):
        response = self.client.put('/api/confidentiality-labels/testname/', {'name': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_single_confidentiality_labels(self):
        response = self.client.get('/api/confidentiality-labels/testname/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_single_confidentiality_labels(self):
        response = self.client.delete('/api/confidentiality-labels/testname/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_confidentiality_datas(self):
        response = self.client.post('/api/confidentiality-datas/', {'name': 'testname2', 'total_docs': 3}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_confidentiality_datas(self):
        response = self.client.get('/api/confidentiality-datas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_single_confidentiality_datas(self):
        response = self.client.put('/api/confidentiality-datas/testname/', {'name': 'testname2', 'total_docs': 4}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_single_confidentiality_datas(self):
        response = self.client.get('/api/confidentiality-datas/testname/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_single_confidentiality_datas(self):
        response = self.client.delete('/api/confidentiality-datas/testname/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


