from django.contrib import admin

from .models import Type, Genre, Content, Image

admin.site.register([Type, Genre, Image, Content])