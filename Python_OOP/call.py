class Call(object):

    def __init__(self, id, name, phone, time, reason):
        self.id = id
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason

    def displayAll(self):
        return 'ID: {} NAME: {} PHONE: {} TIME: {} REASON: {}'.format(
            self.id, self.name, self.phone, self.time, self.reason)
