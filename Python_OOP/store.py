

class Store(object):

    def __init__(self, product, location, owner):
        self.product = product
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.product.append(product)

    def remove_product(self, product):
        self.product.remove(product)

    def inventory(self):
        print self.product


a = Store(product=['apples', 'strawberries', 'pineappe'], location='Mexico', owner='Noel')
a.add_product('grapes')
a.inventory()
a.remove_product('grapes')
a.inventory()
a.remove_product('apples')
