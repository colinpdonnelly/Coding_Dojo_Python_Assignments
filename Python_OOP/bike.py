

class Bike(object):

    def __init__(self, price='$100', max_speed='50 mph', miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        return 'The price is {}, the max speed is {}, and the miles on it is {}'.format(self.price, self.max_speed, self.miles)

    def ride(self):
        self.miles += 10
        return self.miles

    def reverse(self):
        self.miles -= 5
        return self.miles


b = Bike(object)
b.price = 100
print b.miles
print b.max_speed
print b.displayInfo()
print b.ride()
print b.reverse()
print b.ride()
print b.ride()
