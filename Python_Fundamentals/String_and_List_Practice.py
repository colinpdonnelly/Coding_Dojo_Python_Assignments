# 1) Find and replace
str = "It's thanksgiving day. It's my birthday,too!"

print str.find('day')
print str.replace('day', 'month')

# 2) Min and Max
x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

#  3) First and Last
y = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print y[0], y[len(y) - 1]

# 4) New List
z = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
print z
z.sort()
print z
first_list = x[0:len(x) / 2]
second_list = x[len(x) / 2:len(x)]
print "first list", first_list
print "second list", second_list
second_list.insert(0, first_list)
print second_list
