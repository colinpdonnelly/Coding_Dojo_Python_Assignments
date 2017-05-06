# 1) Odd/Even


def odd_even():
    for i in range(1, 2001):
        if i % 2 == 1:
            print i,  "This is an odd number"
        else:
            print i, "This is an even number"


odd_even()

# 2) Multiply


def multiply(arr, num):

    for new in range(0, len(arr)):
        arr[new] *= num
    print arr


numbers_array = [3, 6, 8, 10, 67]
multiply(numbers_array, 5)

# hacker challenge


def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0, x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array


x = layered_multiples(multiply([2, 4, 5], 3))
print x
