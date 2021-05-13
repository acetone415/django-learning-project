from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название песни')
    author = models.CharField(max_length=50, verbose_name='Автор')


class Order(models.Model):
    song = models.ForeignKey('Song')
    congratulation = models.TextField()
    datetime = models.DateTimeField()
