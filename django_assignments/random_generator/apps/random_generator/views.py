from django.shortcuts import render, redirect
import random
import string


def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
    return render(request, 'random_generator/index.html')


def new(request):
    request.session['attempt'] += 1
    request.session['word'] = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(14))
    return redirect('/')
