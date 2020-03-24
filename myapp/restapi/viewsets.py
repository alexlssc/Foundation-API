from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from . import models
from . import serializers


class BooksViewSet(viewsets.ModelViewSet):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BooksSerializer

    permission_classes_by_action = {'create': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser]}

    def create(self, request, *args, **kwargs):
        return super(BooksViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(BooksViewSet, self).partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(BooksViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(BooksViewSet, self).destroy(request, *args, **kwargs)

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

    @action(detail=True)
    def quotes(self, request, pk):
        '''
        Return all the quotes of a specific book
        :return: Response Object
        '''
        book = self.get_object()
        book_id = book.id
        quotes = models.Quotes.objects.all().filter(book=book_id)
        quotes_serializer = serializers.QuotesSerializer(quotes, many=True)
        return Response(quotes_serializer.data)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class ChaptersViewSet(viewsets.ModelViewSet):
    queryset = models.Chapters.objects.all()
    serializer_class = serializers.ChaptersSerializer

    permission_classes_by_action = {'create': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser]}

    def create(self, request, *args, **kwargs):
        return super(ChaptersViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ChaptersViewSet, self).partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ChaptersViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ChaptersViewSet, self).destroy(request, *args, **kwargs)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class CharactersViewSet(viewsets.ModelViewSet):
    queryset = models.Characters.objects.all()
    serializer_class = serializers.CharactersSerializer

    permission_classes_by_action = {'create': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser]}

    def create(self, request, *args, **kwargs):
        return super(CharactersViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(CharactersViewSet, self).partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(CharactersViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(CharactersViewSet, self).destroy(request, *args, **kwargs)

    @action(detail=True)
    def quotes(self, request, pk):
        '''
        Return all the quotes of a specific character
        :return: Response Object
        '''
        character = self.get_object()
        character_id = character.id
        quotes = models.Quotes.objects.all().filter(character=character_id)
        quotes_serializer = serializers.QuotesSerializer(quotes, many=True)
        return Response(quotes_serializer.data)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class QuotesViewSet(viewsets.ModelViewSet):
    queryset = models.Quotes.objects.all()
    serializer_class = serializers.QuotesSerializer

    permission_classes_by_action = {'create': [IsAdminUser],
                                    'partial_update': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser]}

    def create(self, request, *args, **kwargs):
        return super(QuotesViewSet, self).create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(QuotesViewSet, self).partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(QuotesViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(QuotesViewSet, self).destroy(request, *args, **kwargs)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

