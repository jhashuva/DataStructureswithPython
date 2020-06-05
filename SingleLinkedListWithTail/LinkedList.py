from Node import Node
"""A Single linked list"""
class LinkedList:
    """Single Linked List """
    def __init__(self):
        """Create an empty list"""
        self._tail=None
        self._head=None
        self._count=0

    def PushBack(self, data):
        """insert an item to the list"""
        node=Node(data)
        node._next = None
        if  not self._tail:
            self._tail = node
            self._head = self._tail
        else:
            self._tail._next = node
            self._tail = node
        self._count +=1

    def display(self):
        """Display the linked list"""
        item = self._head
        l=list()
        while item:
            l.append(item._data)
            item = item._next
        return l

    def count(self):
        return self._count


    def Find(self,data):
        """Search for the element"""
        item = self._head
        while item:
            if item._data == data:
                return item
            item = item._next
        return None

    def delete(self,data):
        """delete node from the list"""
        current= self._head
        prev = self._head
        while current:
            if current._data==data:
                if current == self._head:
                    self._head = current._next
                else:
                    prev._next = current._next
                self._count-=1
            prev = current
            current = current._next

    def PushFront(self,data):
        node=Node(data)
        node._next=self._head
        self._head = node
        if not self._tail:
            self._tail=self._head
        self._count+=1


    def PopFront(self):
        if not self._head:
            raise Exception("Empty List")
        self._head = self._head._next
        if self._head is None:
            self._tail = None
            self._count-=1

    def PopBack(self):
        if self._head is None:
            raise Exception('Empty List')
        if self._head == self._tail:
            self._tail = None
            self._head = self._tail
        else:
            p= self._head
            while p._next._next:
                p = p._next
            #p = p._next
            p._next = None
            self._tail = p
        self._count-=1

    def AddAfter(self,nd,data):
        node2=Node(data)
        if self.Find(nd):
            node = self.Find(nd)
            node2._next = node._next
            node._next = node2
            if self._tail == node:
                self._tail = node2
            self._count+=1

    def TopFront(self):
        return self._head._data

    def TopBack(self):
        return self._tail._data

    def Empty(self):
        if not self._head:
            return True
        return False