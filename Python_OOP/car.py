

class Car(object):

    def __init__(self, price,    speed, mileage, fuel='full'):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def tax(self):
        if self.price > 10000:
            self.tax = 0.15 * self.price
            self.tax += self.price
            return self.tax
        else:
            self.tax = 0.12 * self.price
            self.tax += self.price
            return self.tax

    def display_all(self):
        return 'Price: {}, Speed: {}, Fuel: {}, Mileage: {}, Tax: {}'.format(self.price, self.speed, self.fuel, self.mileage, self.tax)


c = Car(price=2000, speed='35mph', fuel='full', mileage='15mpg')
print c
c.price
print c.tax()
print c.display_all()
