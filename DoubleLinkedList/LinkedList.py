from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def PushFront(self,data):
        """Insert element at the beginning"""
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        if not self.tail:
            self.head = self.tail

        self.count+=1

    def TopFront(self):
        if not self.head:
            raise Exception('Empty List')
        return self.head.data


    def PopFront(self):
        """Remove an element from the beginnig of the list"""
        if not self.head:
            raise Exception("Empty list")
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.count -= 1

    def PushBack(self,data):
        """Inserting element at the end"""
        node = Node(data)
        if not self.tail:
            self.tail = node
            self.head = self.tail
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count+=1

    def TopBack(self):
        """return last element in the list"""
        if not self.tail:
            raise Exception('Empty list')
        return self.tail.data

    def PopBack(self):
        """Remove the element in the list"""
        if not self.tail:
            raise Exception('Empty List')
        if self.head == self.tail:
            self.tail = None
            self.head = self.tail
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.count -=1

    def Find(self,data):
        """Find the element in the list"""
        if not self.head:
            raise Exception('List is empty')
        item = self.head
        while item:
            if item.data == data:
                return item
            item = item.next
        return None


    def Erase(self,data):
        """remove the element from the list"""
        item = self.head  # head to the item
        node_deleted = False
        if not item:      # there are no elements in the list
            node_deleted = False
        elif item.data == data:    # if the head is the item you want to delete
            self.head = item.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == item.data: # if the tail is the element you want to delete
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while item:
                if item.data == data:
                    item.prev.next = item.next
                    item.next.prev = item.prev
                    node_deleted = True
                item = item.next
        if node_deleted:
            self.count -= 1


    def Empty(self):
        if not self.head:
            return True
        return False


    def AddAfter(self,key,data):
        if self.Find(key):
            node = self.Find(key)
            node2 = Node(data)
            node2.next = node.next
            node2.prev = node
            node.next = node2
            if node2.next:
                node2.next.prev = node2
            if node == self.tail:
                self.tail = node2
            self.count +=1

    def AddBefore(self,key,data):
        if self.Find(key):
            node = self.Find(key)
            node2 = Node(data)
            node2.next = node
            node2.prev = node.prev
            if node2.next:
                node2.prev.next = node2
            if node == self.head:
                self.head = node2
            self.count+=1

    def display(self):
        """Display the linked list"""
        item = self.head
        l = list()
        while item:
            l.append(item.data)
            item = item.next
        return l
