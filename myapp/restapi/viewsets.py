from django.db.models.query import QuerySet
from rest_framework import viewsets
from . import models
from . import serializers


class BooksViewSet(viewsets.ModelViewSet):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BooksSerializer
