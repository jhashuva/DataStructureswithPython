from Node import Node

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def Push(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.count +=1

    def Pop(self):
        if self.head:
            a = self.head.data
            self.head = self.head.next
            self.count -=1
            return a
        else:
            return None

    def Top(self):
        return self.head.data

    def Empty(self):
        if not self.head:
            return True
        return False

    def display(self):
        if self.head:
            current = self.head
            l=[]
            while current:
                l.append(current.data)
                current = current.next
            return l
        else:
            return None

    def max(self):
        if self.head:
            current = self.head
            l = []
            while current:
                l.append(current.data)
                current = current.next
            return max(l)
        else:
            return None

