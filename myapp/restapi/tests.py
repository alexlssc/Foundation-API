import json
from unittest import main

from django.test import TestCase
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from .models import Books, Chapters, Characters


class BookTest(APITestCase):
    def setUp(self):
        self.books = Books(name='Test')
        self.books.save()

    def test_books_creation(self):
        new_data = {
            "name": "testcase",
            "author": "Isaac Asimov",
            "year_published": "1950",
            "isbn": "4729201"
        }
        response = self.client.post(
            '/api/books/',
            data=json.dumps(new_data),
            content_type='application/json'
        )
        self.assertEqual(Books.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_books_get(self):
        response = self.client.get('/api/books/', format=json)
        self.assertEqual(response.data['count'], 1)

    def test_books_get_details(self):
        response_details = self.client.get(
            f'/api/books/{self.books.id}/',
            format=json
        )
        self.assertEqual(response_details.data['name'], "Test")

    def test_books_update(self):
        new_data = {
            "name": "newTestCase",
            "author": "Isaac Asimov",
            "year_published": "1950",
            "isbn": "4729201"
        }
        response = self.client.put(
            f'/api/books/{self.books.id}/',
            data = json.dumps(new_data),
            content_type='application/json',
        )
        self.assertEqual('newTestCase', response.data['name'])

    def test_delete_books(self):
        response = self.client.delete(f'/api/books/{self.books.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ChapterTest(APITestCase):
    def setUp(self):
        self.book = Books(name="Test")
        self.book.save()
        self.chapters = Chapters(book=self.book, chapter_name="chapter_test")
        self.chapters.save()

    def test_chapters_creation(self):
        response = self.client.post(
            '/api/chapters/',
            data=json.dumps({"book": self.book.id, "chapter_name": "newChapterName"}),
            content_type='application/json'
        )
        self.assertEqual(Chapters.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_chapters_get(self):
        response = self.client.get('/api/chapters/', format=json)
        self.assertEqual(response.data['count'], 1)

    def test_books_get_details(self):
        response_details = self.client.get(
            f'/api/chapters/{self.chapters.id}/',
            format=json
        )
        self.assertEqual(response_details.data['chapter_name'], "chapter_test")

    def test_chapters_update(self):
        response = self.client.put(
            f'/api/chapters/{self.chapters.id}/',
            data = json.dumps({"book" : self.book.id, "chapter_name": "newTestCase"}),
            content_type='application/json',
        )
        self.assertEqual('newTestCase', response.data['chapter_name'])

    def test_delete_chapters(self):
        response = self.client.delete(f'/api/chapters/{self.chapters.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_chapters_of_books(self):
        response = self.client.get(
            f'/api/books/{self.book.id}/chapters/',
            format=json
        )
        self.assertEqual(len(response.data), 1)


class CharacterTest(APITestCase):
    def setUp(self):
        self.book1 = Books(name='Book1')
        self.book1.save()
        self.book2 = Books(name='Book2')
        self.book2.save()
        self.character = Characters.objects.create(character_name='CharacterTest')
        self.character.books.set([self.book1, self.book2])
        self.character.save()

    def test_get_characters(self):
        response = self.client.get('/api/characters/', format=json)
        self.assertEqual(response.data['count'], 1)

    def test_get_character_details(self):
        response = self.client.get(f'/api/characters/{self.character.id}/', format=json)
        self.assertEqual(response.data['character_name'], 'CharacterTest')

    def test_characters_update(self):
        valid_new_value = {
            "character_name": "UpdatedTestName",
            "books": [
                self.book1.id,
                self.book2.id
            ]
        }
        response = self.client.put(
            f'/api/characters/{self.character.id}/',
            data=json.dumps(valid_new_value),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['character_name'], 'UpdatedTestName')

    def test_invalid_characters_update(self):
        invalid_new_value = {
            "character_name": "",
            "books": [
                self.book1.id,
                self.book2.id
            ]
        }
        response = self.client.put(
            f'/api/characters/{self.character.id}/',
            data=json.dumps(invalid_new_value),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_characters_delete(self):
        response = self.client.delete(f'/api/characters/{self.character.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_characters_of_books(self):
        response = self.client.get(f'/api/books/{self.book1.id}/characters/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)



