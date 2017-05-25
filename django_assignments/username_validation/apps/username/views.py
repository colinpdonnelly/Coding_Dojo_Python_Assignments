# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.
from .models import Username


def index(request):
    return render(request, 'username/index.html')


def validate(request):
    if request.method == "POST":
        errors = Username.objects.validate(request.POST['email'])
        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            messages.success(
                request, "The username you entered ({}) is valid.  Thank you!".format(request.POST['email']))
            Username.objects.create(email=request.POST['email'])

            return redirect('/success')

    return redirect('/')


def success(request):
    context = {
        'user': Username.objects.all()
    }
    return render(request, 'username/success.html', context)
