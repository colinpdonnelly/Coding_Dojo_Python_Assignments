black = ['* * * *']
red = [' * * * *']
# print black
# print red

for new in range(1, 9):
    if new % 2 == 1:
        print black
    else:
        print ' ', black


star1 = '* * * *'
star2 = ' * * * *'

for new in range(0, 8):
    if new % 2 == 1:
        print star1
    else:
        print star2
