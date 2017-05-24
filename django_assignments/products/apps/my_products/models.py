# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    weight = models.IntegerField(default=1000)
    price = models.IntegerField(default=1000)
    cost = models.IntegerField(default=1000)
    category = models.CharField(max_length=100)
