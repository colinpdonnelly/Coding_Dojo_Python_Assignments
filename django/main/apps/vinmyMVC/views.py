from django.shortcuts import render
# the index function is called when root is visited
# CONTROLLER!!


def index(request):
    print ("*" * 100

           )
    return render(request, "vinmyMVC/index.html")
    # response = "Hello, I am your first request!"
    # return HttpResponse(response)


def show(request):
    print (request.method)
    return render(request, "vinmyMVC/show_users.html")
