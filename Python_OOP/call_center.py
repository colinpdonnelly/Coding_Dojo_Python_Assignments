

class Call(object):

    def __init__(self, idnum, name, phone, time, reason):
        self.idnum = idnum
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason

    def displayAll(self):
        print 'ID: {}'.format(self.idnum)
        print 'NAME: {}'.format(self.name)
        print 'PHONE: {}'.format(self.phone)
        print 'TIME: {}'.format(self.time)
        print 'REASON: {}'.format(self.reason)

        # return self


class CallCenter(object):

    call_list = []
    queue = 0

    def add_call(self, Call):
        # CallCenter.call_list = Call
        CallCenter.queue += 1
        CallCenter.call_list = Call
        print 'The call que is now', CallCenter.queue
        print CallCenter.call_list
        return self

    # def remove_call(self):
    #     CallCenter.call_list[0].pop
    #     return CallCenter.call_list


# a = Call(1, 'Noel', '(999)-999-9999', '12:00PM', 'physical exam')
b = CallCenter()
# c = Call(2, 'Bob', '(000)-000-0000', '12:00PM', 'physical exam')
d = Call(3, 'Bob', '(000)-000-0000', '12:00PM', 'physical exam')
# print a.idnum
# print a.displayAll()
# b.add_call(a.displayAll())
# b.add_call(c.displayAll())
b.add_call(d.displayAll())
print b.call_list
# b.remove_call()
