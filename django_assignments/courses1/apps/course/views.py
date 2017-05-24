# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course


def index(request):
    context = {
        'course': Course.objects.all()
    }
    return render(request, 'course/index.html', context)


def add(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')


def destroy(request, num):
    gotopage = Course.objects.get(id=num)
    context = {
        'course': gotopage
    }

    return render(request, 'course/destroy.html', context)


def eliminate(request, num):
    Course.objects.get(id=num).delete()
    # context = {
    #     'delete': delete_me
    # }
    return redirect('/')
