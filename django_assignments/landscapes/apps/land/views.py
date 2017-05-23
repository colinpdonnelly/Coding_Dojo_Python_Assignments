# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'land/index.html')


def show(request, num):
    # print id
    # print num
    new_num = int(num)
    if 1 < new_num <= 10:
        my_image = {
            'content': 'img/snow.gif'
        }
    elif 11 <= new_num <= 20:
        my_image = {
            'content': 'img/desert.gif'
        }
    elif 21 <= new_num <= 30:
        my_image = {
            'content': 'img/forest.gif'
        }
    elif 31 <= new_num <= 40:
        my_image = {
            'content': 'img/vineyard.gif'
        }
    elif 41 <= new_num <= 50:
        my_image = {
            'content': 'img/tropical.gif'
        }
    else:
        my_image = {
            'content': 'img/else.gif'
        }

    return render(request, 'land/show.html', my_image)
