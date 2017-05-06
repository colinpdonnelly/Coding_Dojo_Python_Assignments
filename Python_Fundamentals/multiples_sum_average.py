# Part 1
for odd in range(1, 1000, 2):
    print odd
# Part 2
for multiples in range(5, 1000000, 5):
    print multiples

# Sum List
a = [1, 2, 5, 10, 255, 3]
sum = 0
avg = 0
for new in a:
    sum += new
    print sum
    avg = sum / 2
    print avg
