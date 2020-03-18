from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from . import models
from . import serializers


class BooksViewSet(viewsets.ModelViewSet):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BooksSerializer

    @action(detail=True)
    def chapters(self, request, pk):
        '''
        Return all the chapters of a specific book
        :return: Response Object
        '''
        book = self.get_object()
        book_id = book.id
        chapters = models.Chapters.objects.all().filter(book_id=book_id)
        chapters_serializer = serializers.ChaptersSerializer(
            chapters, many=True)
        return Response(chapters_serializer.data)

    @action(detail=True)
    def characters(self, request, pk):
        '''
        Return all the characters of a specific book
        :return: Response Object
        '''
        book = self.get_object()
        book_id = book.id
        characters = models.Characters.objects.all().filter(books=book_id)
        characters_serializer = serializers.CharactersSerializer(characters, many=True)
        return Response(characters_serializer.data)


class ChaptersViewSet(viewsets.ModelViewSet):
    queryset = models.Chapters.objects.all()
    serializer_class = serializers.ChaptersSerializer


class CharactersViewSet(viewsets.ModelViewSet):
    queryset = models.Characters.objects.all()
    serializer_class = serializers.CharactersSerializer


class QuotesViewSet(viewsets.ModelViewSet):
    queryset = models.Quotes.objects.all()
    serializer_class = serializers.QuotesSerializer

