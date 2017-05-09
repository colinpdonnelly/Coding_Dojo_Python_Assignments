

class Animal(object):

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        return self.health


a = Animal('Noel')
a.walk().walk().walk().run().run().displayHealth()


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__()
        self.health = 150

    def pet(self):
        self.health += 5
        return self


b = Dog('Corgi')
print b.health
print b.health
print b.name
print b.displayHealth()
b.walk().walk().walk().run().run().pet().displayHealth()


class Dragon(Animal):

    def __init__(self, name):
        super(Dragon, self).__init__()
        self.health = 170

    def fly(self):
        self.health -= 10
        return self


c = Dragon('Blue Eyes White Dragon')
c.health
c.walk().walk().walk().run().fly().fly().displayHealth()
