from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=150)


class Chapters(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=300)
