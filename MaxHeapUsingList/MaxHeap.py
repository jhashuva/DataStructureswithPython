class Heap:
    def __init__(self):
        self.__array = []
        self.__last_index = -1

    def push(self,data):
        self.__array.append(data)
        self.__last_index +=1
        self.__siftup(self.__last_index)


    def extractMax(self):
        if self.__last_index == -1:
            raise Exception('Empty Heap')
        root_value = self.__array[0]
        if self.__last_index>0:
            self.__array[0]= self.__array[self.__last_index]
            self.__siftdown(0)
        self.__last_index -=1
        return root_value

    def getMax(self):
        if not self.__array:
            return None
        return self.__array[0]

    def changePriority(self,data,new_data):
        data_index = self.__get_index(data)
        if data_index!= -1:
            self.__array[data_index] = new_data
            if self.__last_index !=data_index:
                self.__siftup(data_index)
                self.__siftdown(data_index)

    def __get_index(self,data):
        if self.__last_index == -1:
            return -1
        for i, val in enumerate(self.__array):
            if val == data:
                return i
        return -1


    def __get_parent_withIndex(self,index):
        if index == 0:
            return None, None
        parent_index = (index-1)//2
        return parent_index, self.__array[parent_index]

    def comparer(self,value1,value2):
        if value1 > value2:
            return True
        return False

    def __siftup(self,index):
        current_value = self.__array[index]
        parent_index, parent_value = self.__get_parent_withIndex(index)
        if index > 0 and self.comparer(current_value, parent_value):
            self.__array[parent_index],self.__array[index]=current_value,parent_value
            self.__siftup(parent_index)

    def __siftdown(self,index):
        current_value = self.__array[index]
        left_child_index,left_child = self.__get_left(index)
        right_child_index, right_child = self.__get_right(index)
        best_child_index, best_child_value = (right_child_index,right_child) if right_child_index is not None and self.comparer(right_child, left_child) else (left_child_index, left_child)
        if best_child_index is not None and self.comparer(best_child_value,current_value):
            self.__array[index], self.__array[best_child_index] = best_child_value,current_value
            self.__siftdown(best_child_index)
        return

    def __get_left(self,index):
        left_child_index = 2*index + 1
        if left_child_index > self.__last_index:
            return None, None
        return left_child_index, self.__array[left_child_index]

    def __get_right(self,index):
        right_child_index = 2*index + 2
        if right_child_index > self.__last_index:
            return None,None
        return right_child_index, self.__array[right_child_index]