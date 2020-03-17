from django.db import models


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
