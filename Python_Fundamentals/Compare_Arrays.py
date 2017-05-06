

def compare(list_one, list_two):
    # list_one = [1, 2, 5, 6, 2]
    # list_two = [1, 2, 5, 6, 2]

    for element in list_one:
        if element in list_two:
            print "Identical"
        else:
            print "Non-identical"


compare([1, 3, 5, 6, 2], [1, 2, 5, 6, 2])
