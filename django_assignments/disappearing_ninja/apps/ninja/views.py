from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
    return render(request, 'ninja/index.html')


def ninja(request):
    # context = {
    #     'url': 'img/tmnt.png'
    # }
    return render(request, 'ninja/ninja.html')


def all_ninja(request, color):
    color = {
        'color': color
    }
    return render(request, "ninja/ninja.html", color)
