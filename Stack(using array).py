                            #implementation of Stack using Array
class Stack:
    def __init__(self):
        self.top = []

    def peek(self):
        return self.top[len(self.top) - 1]

    def push(self, value):
        self.top.append(value)
        return self.top

    def pop(self):
        if len(self.top) == 0:
            return None
        else:
            del self.top[len(self.top) - 1]
            return self.top

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
