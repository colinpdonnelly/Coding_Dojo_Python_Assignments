from django.shortcuts import render, redirect
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = ''
    return render(request, 'ninja/index.html')


def process(request):
    # if request.method == "POST":
    choice = request.POST['choice']
    if choice == 'farm':
        gold = random.randrange(10, 20)
    elif choice == 'cave':
        gold = random.randrange(5, 10)
    elif choice == 'house':
        gold = random.randrange(2, 5)
    else:
        gold = random.randrange(-50, 51)

    if (gold > 0):
        text = "Earned " + str(gold) + 'golds from the ' + choice + '!'
    elif (gold < 0):
        text = 'Ouch! You entered a ' + choice + ' and lost ' + str(gold) + ' golds!'

    request.session['gold'] += gold
    request.session['activities'] += text + '\n'

    return redirect('/')

    # if (choice == 'farm'):
    #     request.session['gold'] += random.randrange(10, 20)
    # if (choice == 'cave'):
    #     request.session['gold'] += random.randrange(5, 10)
    # if (choice == 'house'):
    #     request.session['gold'] += random.randrange(2, 5)
    # if (choice == 'casino'):
    #     if random.randrange(1, 3) == 1:
    #         request.session['gold'] += random.randrange(0, 50)
    #     elif random.randrange(1, 3) == 2:
    #         request.session['gold'] -= random.randrange(0, 50)
    #
    # request.session['activities'] + = ''
