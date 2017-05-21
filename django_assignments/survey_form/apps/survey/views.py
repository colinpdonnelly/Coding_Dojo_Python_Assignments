from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'survey_form/index.html')


def survey(request):
    request.session['attempt'] += 1
    request.session['my_name'] = request.POST['my_name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')


def result(request):

    return render(request, 'survey_form/result.html')
