# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Book


def index(request):
    context = {
        'book': Book.objects.all()
    }

    return render(request, 'stack/index.html', context)


def add(request):
    # print Book.objects.all()
    # request.session['my_id'] = request.POST['my_id']
    Book.objects.create(
        # id=request.POST['my_id'],
        title=request.POST['title'], category=request.POST['category'], author=request.POST['author'])

    return redirect('/')


def remove(request):
    # Book.objects.filter(id=id).delete
    # b = Book.objects.get(id=1)
    Book.objects.all().delete()
    # b.delete()
    return redirect('/')
