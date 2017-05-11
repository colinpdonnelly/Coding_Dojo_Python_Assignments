

class Animal(object):

    def __init__(self, name='Animal', health=100):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        return self.name + ': ' + str(self.health)


a = Animal('Noel')
print a.walk().walk().walk().run().run().displayHealth()


class Dog(Animal):

    # def __init__(self, name='Dog', health=150):
    #     super(Dog, self).__init__(name, health)

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

    def __init__(self, name='Dragon', health=170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print 'this is a dragon'
        super(Dragon, self).displayHealth()
        return self


c = Dragon('Blue Eyes White Dragon')
c.health
print c.walk().walk().walk().run().fly().fly().displayHealth()
