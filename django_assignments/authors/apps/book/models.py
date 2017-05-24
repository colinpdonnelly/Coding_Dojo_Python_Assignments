# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from apps.book.models import Books
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Books(models.Model):
    author_id = models.ForeignKey(Author)
    name = models.CharField(max_length=100)
    published_date = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    in_print = models.BooleanField(default=True)
