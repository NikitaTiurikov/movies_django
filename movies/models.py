from django.db import models
from django.db.models import Model
from pkg_resources import require


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=255)
    type = models.ForeignKey(Type, models.PROTECT)
    genre = models.ForeignKey(Genre, models.PROTECT)
    trailer = models.URLField()
    description = models.TextField()
    rating = models.FloatField()
    image = models.OneToOneField(Image, models.PROTECT)
    country = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Registration(models.Model):
    login = models.CharField(max_length=255, unique=True, verbose_name='Логін')
    name = models.CharField(max_length=255, verbose_name='Імʼя')
    pwd = models.CharField(max_length=255, verbose_name='Пароль')