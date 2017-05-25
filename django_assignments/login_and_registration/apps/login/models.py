# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UserManager(models.Manager):
    def validate(self, first_name, last_name, email, password, pconfirm):
        errors = []

        if len(first_name) < 2:
            errors.append('First name must contain more than 2 characters')
        if len(last_name) < 2:
            errors.append('Last name must contain more than 2 characters')
        if len(email) <= 0:
            errors.append('Please enter an email')
        if len(password) < 8:
            errors.append('Password must contain more than 8 characters')
        if password != pconfirm:
            errors.append('Please enter the same password')
        check_email = self.filter(email=email)
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
