

class Product(object):

    def __init__(self, price, item_name, weight, brand, cost=0.0, status='for sale'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self):
        self.add_tax = 0.15 * self.price
        self.add_tax += self.price
        self.price = self.add_tax
        return float(self.price)

    def return_me(self):
        if self.status == 'defective':
            self.cost *= 0.0
            return self.cost
        elif self.status == 'opened':
            self.return_me = self.price * .20
            self.cost = self.add_tax() - self.return_me
            return self.cost
        else:
            return self.add_tax()

    def display_info(self):
        print 'Status:{} Cost:{}'.format(self.status, self.return_me())
        return 'Price w/ Tax: {}, Item: {}, Weight: {}, Brand: {}'.format(self.price, self.item_name, self.weight, self.brand)


a = Product(price=50.0, item_name='t-shirt', weight=0.2,
            cost=0.0, brand='diamond', status='defective')
b = Product(price=50.0, item_name='t-shirt', weight=0.2, cost=0.0, brand='diamond', status='opened')
c = Product(price=100.0, item_name='t-shirt', weight=0.2, cost=0.0, brand='diamond', status='none')
d = Product(price=20.0, item_name='t-shirt', weight=0.2, cost=0.0, brand='diamond', status='opened')

# b.price
# b.cost
# b.status
# b.add_tax()
# b.price
# b.return_me()
print b.display_info()
print a.display_info()
print c.display_info()
print d.display_info()
