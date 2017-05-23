from django.shortcuts import render
from .models import People


def index(request):
    People.objects.create(first_name="Mike", last_name="Hannon")
    people = People.objects.all()
    print (people)
    return render(request, "first_app/index.html")
