from django.shortcuts import render


def index(request):
    context = {
        'greeting': 'hello world',
        'bye': 'goodbye world'
    }
    return render(request, 'portfolio/index.html', context)
    # Create your views here.


def testimonials(request):
    print(request.method)
    return render(request, 'portfolio/testimonials.html')


def projects(request):
    return render(request, 'portfolio/projects.html')


def about(request):
    return render(request, 'portfolio/about.html')
