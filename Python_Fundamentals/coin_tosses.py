import random


def c_toss(num):
    head = 0
    tail = 0
    for x in range(1, num):
        generator = random.randint(0.0, 1.0)
        if generator == 1:
            head += 1
            print 'Attempt #', x, 'Heads'
        else:
            tail += 1
            print 'Attempt #', x, 'Tails'
    print "Done! You had this many heads", head, "and this many tails", tail


c_toss(5001)
