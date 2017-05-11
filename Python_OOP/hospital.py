

class Hospital(object):

    def __init__(self, hospital):
        self.patients = ['None', 'None', 'None']
        self.hospital = hospital
        self.capacity = 2
        self.list = 0
        self.bednum = 0

    def admit(self, name):
        for i in range(1, self.capacity):
            if self.patients[i] == 'None':
                self.patients[i] = name
                print 'bed number is', i
            return self
            # self.list += 1
        # self.bednum += 1

    def discharge(self, num):
        for name2 in range(len(self.patients)):
            if self.patients[name2].idnum == num:
                # print self.patients[name2]
                self.patients.pop(name2)
                # self.bednum -= 1
            return self

    def info(self):
        for name1 in range(len(self.patients)):
            print 'Name:' + self.patients[name1].name
            print 'ID:' + str(self.patients[name1].idnum)
            print 'Allergies:' + self.patients[name1].allergies
            print 'You are bed number', self.bednum
        if self.list == self.capacity:
            print 'Hosital is at the full capacity', self.capacity
        return self


class Patient(object):

    def __init__(self, idnum, name, allergies):
        self.idnum = idnum
        self.name = name
        self.allergies = allergies
        self.bednum = 0

    def displayAll(self):
        print self.idnum
        print self.name
        print self.allergies
        print self.bednum


a = Patient(1, 'Noel', 'Cheese')
b = Patient(2, 'Morty', 'Dogs')
c = Patient(3, 'Rick', 'Cats')
# a.displayAll()
my_hospital = Hospital('UCLA')
my_hospital.admit(a)
my_hospital.admit(b)
# my_hospital.admit(c)
# my_hospital.discharge(1)
# my_hospital.patients
print my_hospital.info()
