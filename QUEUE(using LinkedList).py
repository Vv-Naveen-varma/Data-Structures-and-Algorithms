                #implementation of Queue using LinkeList
class Queue:
    def __init__(self):
        self.first = {'value':None,'next':None}
        self.last = self.first
        self.length = 0

    def peek(self):
        return self.first

    def Node(self, value):
        node = {
            'value': value,
            'next': None
        }
        return node

    def enqueue(self, value):
        newNode = self.Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = self.first
        else:
            self.last['next'] = newNode
            self.last = newNode
        self.length += 1
        return self.first

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            self.first = self.first['next']
            self.length -= 1
            return self.first

q = Queue()
print(q.enqueue(100))
print(q.enqueue(200))
print(q.enqueue(300))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
