from __future__ import unicode_literals

from django.db import models

class Rols(models.Model):
    rol = models.CharField(max_length=20, null = False, default = None)

class User(models.Model):
    name = models.CharField(max_length=50, null = False, default = None)
    username = models.CharField(max_length=20, null = False, default = None)
    password = models.CharField(max_length=200,null = False, default = None)
    rol_id = models.ForeignKey(Rols, on_delete=models.CASCADE, null = False, default = None)

class Article(models.Model):
    content = models.TextField(null = False, default = None)
    photo = models.CharField(max_length=20, null = False, default = None)

class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null = False, default = None)
    user = models.CharField(max_length = 20, null = False, default = None)
    comment = models.TextField(null = False, default = None)

    