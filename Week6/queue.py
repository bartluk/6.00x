class Queue(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        self.vals.append(e)

    def remove(self):
        try:
            self.vals.pop(0)
        except:
            raise ValueError

    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

q1 = Queue() 
q2 = Queue() 
q1.insert(17) 
q2.insert(20) 
q1.remove() 
q2.remove()