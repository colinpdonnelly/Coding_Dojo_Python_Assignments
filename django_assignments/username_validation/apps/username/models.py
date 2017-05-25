# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserManager(models.Manager):
    def validate(self, email):
        errors = []

        if len(email) < 8:
            errors.append('Username is not valid')
        if len(email) > 30:
            errors.append('Username is not valid')
        return errors


class Username(models.Model):
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=1000)
    objects = UserManager()
