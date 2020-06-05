import array
class Stack:

    def __init__(self):
        self.array = array.array('i',[])
        self.count = 0

    def Push(self,data):
        self.array.append(data)
        self.count +=1

    def Top(self):
        if not self.array:
            return None
        return self.array[-1]

    def Pop(self):
        a = self.array.pop()
        self.count-=1
        return a

    def Empty(self):
        if not self.array:
            return True
        return False

    def max(self):
        return max(self.array)

    def display(self):
        return self.array