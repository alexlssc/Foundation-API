import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


class CreateBookTest(APITestCase):
    def setUp(self):
        self.valid_payload = {
            "name": "testName"
        }

        self.invalid_payload = {
            "name": ""
        }

    def test_create_valid_book(self):
        response = self.client.post(
            '/api/books/', data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_book(self):
        response = self.client.post(
            '/api/books/', data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetBookTest(APITestCase):
    def setUp(self):
        self.valid_payload = {
            "name": "testName"
        }
        response = self.client.post(
            '/api/books/', data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results']
                         [0]['name'], self.valid_payload["name"])


class UpdateBookTest(APITestCase):
    def setUp(self):
        self.valid_payload = {
            "name": "testName"
        }
        self.new_valid_payload = {
            "name": "updatedName"
        }
        self.new_invalid_payload = {
            "name": ""
        }
        response = self.client.post(
            '/api/books/', data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_valid_update_books(self):
        response = self.client.put(
            '/api/books/4/', data=json.dumps(self.new_valid_payload), content_type='application/json')
        response_get = self.client.get('/api/books/4/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response_get.data['name'], self.new_valid_payload['name'])

    def test_invalid_update_books(self):
        response = self.client.put(
            '/api/books/3/', data=json.dumps(self.new_invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
