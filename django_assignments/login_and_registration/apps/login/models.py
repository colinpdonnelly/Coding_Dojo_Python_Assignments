# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re


class UserManager(models.Manager):
    def validate(self, post):
        errors = []

        if len(post['first_name']) < 2:
            errors.append('First name must contain more than 2 characters')
        if len(post['last_name']) < 2:
            errors.append('Last name must contain more than 2 characters')
        if len(post['email']) <= 0:
            errors.append('Please enter an email')
        if len(post['password']) < 8:
            errors.append('Password must contain more than 8 characters')
        if post['password'] != post['pconfirm']:
            errors.append('Please enter the same password')
        check_email = self.filter(email=post['email'])
        if check_email:
            errors.append('Email already exists in the database.')
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    pconfirm = models.CharField(max_length=500)
    objects = UserManager()
