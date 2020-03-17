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
        Returns all chapters of a specific book
        '''
        book = self.get_object()
        book_id = book.id
        chapters = models.Chapters.objects.all().filter(book_id=book_id)
        chapters_serializer = serializers.ChaptersSerializer(
            chapters, many=True)
        return Response(chapters_serializer.data)


class ChaptersViewSet(viewsets.ModelViewSet):
    queryset = models.Chapters.objects.all()
    serializer_class = serializers.ChaptersSerializer
