

class Call(object):

    def __init__(self, idnum, name, phone, time, reason):
        # Call Setup
        self.idnum = idnum
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason

    def displayAll(self):
        # Displays all of my caller's information
        print 'ID: {}'.format(self.idnum)
        print 'NAME: {}'.format(self.name)
        print 'PHONE: {}'.format(self.phone)
        print 'TIME: {}'.format(self.time)
        print 'REASON: {}'.format(self.reason)

        # return self


class CallCenter(object):

    def __init__(self, calls):
        self.calls = calls
        self.queue_size = len(calls)

    def add(self, idnum,  name, phone, time, reason):
        new_call = Call(idnum,  name, phone, time, reason)
        self.calls.append(new_call)
        return self

    def info(self):
        for call in self.calls:
            print call.idnum
            print call.name
            print call.phone
            print call.phone
            print call.time
            print call.reason

        print 'The length of the que is', self.queue_size
        return self

    def remove(self):
        for idx in range(0, len(self.calls) - 1):
            self.calls[idx] = self.calls[idx + 1]
        self.calls.pop()
        return self

    def find_and_remove(self, phone_number):
        for idx in range(0, len(self.calls)):
            if self.calls[idx].caller_phone_number == phone_number:
                for idx2 in range(idx, len(self.calls) - 1):
                    self.calls[idx2] = self.calls[idx2 + 1]
                self.calls.pop()
                break
        return self

    def sort(self):
        pass


# a = Call(1, 'Noel', '(999)-999-9999', '12:00PM', 'physical exam')
d = Call(3, 'Bob', '(000)-000-0000', '12:00PM', 'physical exam')

b = CallCenter([d])
# c = Call(2, 'Bob', '(000)-000-0000', '12:00PM', 'physical exam')
# print b.info()
b.calls
b.add(3, 'Bob', '(000)-000-0000', '12:00PM', 'physical exam')
print b.info()
print b.calls
b.remove()
print b.info()
b.remove()
print b.info()
b.remove()
