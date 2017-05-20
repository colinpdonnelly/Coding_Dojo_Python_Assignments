from django.shortcuts import render


def index(request):
    return render(request, 'portfolio/index.html')
    # Create your views here.


def testimonials(request):
    print(request.method)
    return render(request, 'portfolio/testimonials.html')


def projects(request):
    return render(request, 'portfolio/projects.html')


def about(request):
    return render(request, 'portfolio/about.html')
