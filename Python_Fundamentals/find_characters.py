l = ['hello', 'world', 'my', 'name', 'is', 'Anna']

for x in l:
    for new in x:
        if new.endswith('o'):
            print x

l = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'

for find in l:
    for new in find:
        if new == char:
            print find
