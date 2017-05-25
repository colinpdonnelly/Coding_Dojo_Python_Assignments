# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt


def index(request):

    return render(request, 'login/index.html')


def register(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            messages.success(request, "Success! Welcome, {}".format(
                request.POST['first_name']))
            hashed_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(
                first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pass, pconfirm=request.POST['pconfirm'])
            return redirect('/success')
    return redirect('/')


def login(request):
    if request.method == "POST":
        users = User.objects.filter(email=request.POST['email'])
        if users:
            user = users[0]
            hashed_pass = bcrypt.hashpw(request.POST['password'].encode(), user.password.encode())
            if user.password == hashed_pass:
                messages.success(request, "You have successfully logged in!")
                request.session['logged_user'] = user.id
                return redirect('/success')
        messages.error(request, 'Invalid authenication credentials')
    return redirect('/')


def success(request):
    context = {
        'my_users': User.objects.all()
    }
    return render(request, 'login/success.html', context)
