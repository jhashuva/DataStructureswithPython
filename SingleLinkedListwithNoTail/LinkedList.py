from Node import Node
class LinkedList:
    """SLL with no tail refrence"""
    def __init__(self):
        self.head=None
        self.count=0

    def PushFront(self,data):
        """Add the element at the beginning of the list"""
        node = Node(data)
        node.next=self.head
        self.head = node
        self.count+=1

    def PopFront(self):
        """Remove element at the end of the list"""
        if not self.head:
            raise Exception('Empty List')
        self.head = self.head.next
        self.count-=1

    def PushBack(self,data):
        """Add the element at the end of the list"""
        node = Node(data)
        item = self.head
        while item.next:
            item = item.next
        item.next = node
        self.count+=1

    def PopBack(self):
        """It will remove last node from the list"""
        if not self.head:
            raise Exception('Empty List')
        p=self.head
        while not p.next.next:
            p = p.next
        p.next = None
        self.count-=1

    def AddAfter(self,node,data):
        """Add  node after specified node"""
        node2= Node(data)
        node = Node(data)
        node2.next = node.next
        node.next = node2
        self.count+=1

    def Find(self,data):
        """To find the node in the list"""
        item = self.head
        while item:
            if item.data == data :
                return True
            item = item.next
        return False

    def nodes(self):
        """It will return number of nodes within the list"""
        return self.count


    def Empty(self):
        """This will check whether a list is emty or not"""
        if not self.head:
            return True
        return False

    def TopBack(self):
        item =self.head
        value =None
        while item:
            value = item
            item = item.next
        return value.data

