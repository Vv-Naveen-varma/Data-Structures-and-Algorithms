class LinkedList:
    def __init__(self, value):
        self.head = {
            'value':value,
            'next':None
        }
        self.tail = self.head
        self.length = 1

    def node(self,value):
        node = {
            'value': value,
            'next': None
        }
        return node

    def append(self,value):
        new_node = self.node(value)
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self.head

    def prepend(self,value):
        new_node = self.node(value)
        new_node['next'] = self.head
        self.head = new_node
        self.length += 1
        return self.head

    def printlist(self):
        listofvalues = []
        currentNode = self.head
        while currentNode != None:
            listofvalues.append(currentNode['value'])
            currentNode = currentNode['next']
        print(listofvalues)
        return listofvalues

    def insert(self, value, index):
        newNode = self.node(value)
        if index == 0:
            self.prepend(value)
            return self.printlist()
        elif index >= self.length:
            self.append(value)
            return self.printlist()
        else:
            leader = self.traversetoIndex(index-1)
            newNode['next'] = leader['next']
            leader['next'] = newNode
            self.length += 1
            return self.printlist()

    def traversetoIndex(self,index):
        count = 0
        currentNode = self.head
        while count != index:
            currentNode = currentNode['next']
            count += 1
        return currentNode

    def remove(self, index):
        if index == 0:
            self.head = self.head['next']
            return self.printlist()
        else:
            leader = self.traversetoIndex(index-1)
            removeNode = leader['next']
            attachNode = removeNode['next']
            leader['next'] = attachNode
            self.length -= 1
            return self.printlist()


l = LinkedList(10)
l.append(5)
l.append(16)
l.prepend(1)
l.printlist()
l.insert(2,3) #insert 2 at index 3
l.remove(4) # remove at index 2