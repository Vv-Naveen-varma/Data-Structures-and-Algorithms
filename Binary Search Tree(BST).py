                                         # Binary Sreach Tree (BST) implementation using LinkedList(Python)
class BinarySearchTree:
    def __init__(self):
        self.root = {'left':None, 'value':None, 'right': None}

    def Node(self, value):
        node = {'left':None, 'value':value, 'right': None}
        return node

    def insert(self, value):
        newNode = self.Node(value)
        if self.root['value'] == None:
            self.root = newNode
            return self.root
        else:
            currentNode = self.root
            while True:
                if value < currentNode['value']:                # left
                    if currentNode['left'] == None:
                        currentNode['left'] = newNode
                        return self.root
                    else:
                        currentNode = currentNode['left']
                else:                                           # right
                    if currentNode['right'] == None:
                       currentNode['right'] = newNode
                       return self.root
                    else:
                        currentNode = currentNode['right']

    def lookup(self, value):
        currentNode = self.root
        if self.root['value'] == None:
            return 'Not Found'
        while True:
            if currentNode == None:
                return 'Not Found'
            if value == currentNode['value']:
                return 'Found'
            if value > currentNode['value']:
                currentNode = currentNode['right']
            if value < currentNode['value']:
                currentNode = currentNode['left']

    def remove(self, value):                                                                          # removing a vlaue from the Tree
        notFound = self.lookup(value)
        if notFound == 'Not Found':
            return notFound
        else:
            if self.root['value'] == value:                                                           # if currentNode is the root
                if self.root['right'] != None and self.root['left'] != None:                          # if root has two childs
                    return self.removing_Node_With_Two_Childs(self.root)
                if self.root['right'] == None and self.root['left'] != None:                          # if root has only left subtree
                    self.root = self.root['left']
                    return self.root
                if self.root['left'] == None and self.root['right'] != None:                          # if root has only right subtree
                    self.root = self.root['right']
                    return self.root
            parentNodeOfvalue = self.traverse(value)
            if parentNodeOfvalue['right'] != None and parentNodeOfvalue['right']['value'] == value:   # if currentNode is the rightChild
                return self.removingRightChild(parentNodeOfvalue)
            if parentNodeOfvalue['left'] != None and parentNodeOfvalue['left']['value'] == value:     # if currentNode is the leftChild
                return self.removingLeftChild(parentNodeOfvalue)

    def removing_Node_With_Two_Childs(self, currentNode):
        successor = self.successorOf(currentNode)
        temp = successor['value']
        self.remove(successor['value'])
        currentNode['value'] = temp
        return self.root

    def removingRightChild(self, parentNodeOfvalue):
        currentNode = parentNodeOfvalue['right']
        if currentNode['right'] == None and currentNode['left'] == None:        # removing leafNode
            parentNodeOfvalue['right'] = None
            return self.root
        elif currentNode['left'] == None and currentNode['right'] != None:      # removing a Node with one Child(who is right)
            parentNodeOfvalue['right'] = currentNode['right']
            return self.root
        elif currentNode['right'] == None and currentNode['left'] != None:      # removing a node with one Child(who is left)
            parentNodeOfvalue['right'] = currentNode['left']
            return self.root
        else:                                                                   # removing a node with two childs
            return self.removing_Node_With_Two_Childs(currentNode)


    def removingLeftChild(self, parentNodeOfvalue):
        currentNode = parentNodeOfvalue['left']
        if currentNode['right'] == None and currentNode['left'] == None:        # removing leafNode
            parentNodeOfvalue['left'] = None
            return self.root
        elif currentNode['right'] == None and currentNode['left'] != None:      # removing a node with oneChild(who is left)
            parentNodeOfvalue['left'] = currentNode['left']
            return self.root
        elif currentNode['left'] == None and currentNode['right'] != None:      # removing a Node with oneChild(who is right)
            parentNodeOfvalue['left'] = currentNode['right']
            return self.root
        else:                                                                   # removing a node with Two childs
            return self.removing_Node_With_Two_Childs(currentNode)

    def successorOf(self, currentNode):                                         # finding the successor of a node
        successor = currentNode['right']
        while True:
            if successor['left'] == None:
                return successor
            successor = successor['left']

    def traverse(self, value):                                                  # finding the ParentNode of the value
        currentNode = self.root
        while True:
            if value > currentNode['value']:
                if currentNode['right']['value'] == value:
                    return currentNode
                currentNode = currentNode['right']
                if currentNode['right'] != None and currentNode['right']['value'] == value:
                    return currentNode
                if currentNode['left'] != None and currentNode['left']['value'] == value:
                    return currentNode
            if value < currentNode['value']:
                if currentNode['left']['value'] == value:
                    return currentNode
                currentNode = currentNode['left']
                if currentNode['left'] != None and currentNode['left']['value'] == value:
                    return currentNode
                if currentNode['right'] != None and currentNode['right']['value'] == value:
                    return currentNode
            if value == currentNode['value']:
                return currentNode


t = BinarySearchTree()
t.insert(9)
t.insert(20)
t.insert(4)
t.insert(1)
t.insert(15)
t.insert(6)
t.insert(70)
t.insert(50)
t.insert(60)
print(t.insert(10))         #inserting values into BST
print(t.lookup(9))
print(t.lookup(60))
print(t.remove(6))          #removing a leaf node
print(t.remove(4))          #removing a node with one child
print(t.remove(20))         #removing a node with Two childs
print(t.remove(9))          #removing the root node
