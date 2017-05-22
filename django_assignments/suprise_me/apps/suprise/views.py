# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random

myList = ['hello', 'world', 'good', 'bye', 'hungry', 'food', 'eating', 'poop']


def index(request):
    return render(request, 'suprise/index.html')


def suprise(request):
    return render(request, 'suprise/suprise.html')


def my_list(request):
    request.session['num'] = int(request.POST['num'])
    newList = []
    # for new in myList:
    #     new.append(newList)
    #     print newList
    # for new in myList:
    #     newList.append(new)
    #     print newList
    # for new in range(0, request.session['num']):
    while len(newList) != request.session['num']:
        word = random.choice(myList)
        if word not in newList:
            newList.append(word)
        print newList
        # newList.append(myList[new])
        # random.choice.newList
        # # newList.append(new1)
        request.session['list'] = newList

        # request.POST['num'] * VALUES
        # print i
    return redirect('/suprise')
