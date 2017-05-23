from django.shortcuts import render, redirect
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


def create(request):
    print(request.method)
    if request.method == "POST":
        print ("*" * 10)
        print (request.POST)
        print ("*" * 10)

        request.session['name'] = request.POST['first_name']
        return redirect('/')
    else:
        return redirect('/')
