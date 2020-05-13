class DoubleLinkedList:
    def __init__(self, value):
        self.head = {
            'previous': None,
            'value':value,
            'next':None
        }
        self.tail = self.head
        self.length = 1

    def node(self,value):
        node = {
            'previous': None,
            'value': value,
            'next': None
        }
        return node

    def append(self,value):
        new_node = self.node(value)
        new_node['previous'] = self.tail
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self.head

    def prepend(self,value):
        new_node = self.node(value)
        new_node['next'] = self.head
        self.head['previous'] = new_node
        self.head = new_node
        self.length += 1
        return self.printlist()

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
            nextofleader = leader['next']
            newNode['next'] = nextofleader
            newNode['previous'] = leader
            leader['next'] = newNode
            nextofleader['previous'] = newNode
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
            self.head['previous'] = None
            self.length -= 1
            return self.printlist()
        elif index == self.length-1:
            self.tail['previous']['next'] = None
            self.length -= 1
            return self.printlist()
        else:
            leader = self.traversetoIndex(index-1)
            removeNode = leader['next']
            attachNode = removeNode['next']
            attachNode['previous'] = leader
            leader['next'] = attachNode
            self.length -= 1
            return self.printlist()


l = DoubleLinkedList(10)
l.append(16)
l.append(5)
l.append(50)
l.prepend(1)
l.insert(2,3) #insert 2 at index 3
l.remove(2) # remove at index 2
print(l.length)
