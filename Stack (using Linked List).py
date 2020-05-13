                                        #Implementation of Stack using LinkedList
class Stack:
    def __init__(self):
        self.top = {'value':None,'next':None}
        self.bottom = self.top
        self.length = 0

    def Node(self, value):
        node = {
            'value': value,
            'next': None
        }
        return node

    def peek(self):
        return self.top

    def push(self, value):
        newNode = self.Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holder = self.top
            self.top = newNode
            self.top['next'] = holder
        self.length += 1
        return self.top

    def pop(self):
        if self.length == 0:
            return None
        else:
            holder = self.top
            self.top = self.top['next']
            self.length -= 1
            return holder['value']

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.peek())
