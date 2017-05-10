x = ['magicalunicorns', 19, 'hello', 98.98, 'world']


def typelist(x):

    for new in x:
        if isinstance(new, str):
            print "String:", new


typelist(x)


def new_list(a):
    if isinstance(a, int):
        print "Big list", a
    else:
        print "Short list", a


new_list([4, 34, 22, 68, 9, 13, 3, 5, 7, 9, 2, 12, 45, 923])
