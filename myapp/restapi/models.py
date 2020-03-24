from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Books(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    year_published = models.CharField(max_length=4)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Chapters(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=300)

    def __str__(self):
        return self.chapter_name


class Characters(models.Model):
    books = models.ManyToManyField(Books)
    character_name = models.CharField(max_length=200)

    def __str__(self):
        return self.character_name


class Quotes(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    citation = models.TextField()

    def __str__(self):
        return self.citation
