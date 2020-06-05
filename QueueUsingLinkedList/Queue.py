from Node import Node
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        node = Node(data)
        if not self.tail:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if not self.head:
            raise Exception('Queue is empty')
        else:
            self.head = self.head.next

    def empty(self):
        if not self.head:
            return True
        return False

    def display(self):
        current = self.head
        l=[]
        if self.head:
            while current:
                l.append(current.data)
                current = current.next
            return l
        else:
            return l