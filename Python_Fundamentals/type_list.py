x = ['magicalunicorns', 19, 'hello', 98.98, 'world']


def typelist(x):

    for new in x:
        if isinstance(new, str):
            print "String:", new
