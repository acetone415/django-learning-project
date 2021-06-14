from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название песни')
    author = models.CharField(max_length=50, verbose_name='Автор',
                              db_index=True)

    def __str__(self):
        return f'{self.author} - {self.title}'

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        ordering = ['author', 'title']


class Order(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE,
                             verbose_name='Песня')
    congratulation = models.TextField(null=True, blank=True,
                                      verbose_name='Текст поздравления')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Текст поздравления')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-published']
