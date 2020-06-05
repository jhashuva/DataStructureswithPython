from array import array
class Queue:
    def __init__(self):
        self.array = array('i',[])
        self.read = None
        self.write = None

    def enqueue(self,data):
        self.array.append(data)

    def dequeue(self):
        if self.array:
            del self.array[0]

    def empty(self):
        if not self.array:
            return True
        return False

    def display(self):
        return self.array


