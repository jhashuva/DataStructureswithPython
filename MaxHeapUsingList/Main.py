from MaxHeap import Heap
heap = Heap()
a="""
1. Push
2. Get Max
3. Delete Max
4. Change Priority"""

while True:
    print(a)
    choice = int(input('Enter your choice: '))
    if choice ==1 :
        a= int(input('Enter the data to insert: '))
        heap.push(a)
    elif choice == 2:
        print(f'Max value in the heap is {heap.getMax()}')
    elif choice == 3:
        heap.extractMax()
    elif choice == 4:
        dat = int(input('Enter the value to change its priority'))
        priority = int(input(f'Enter the changed priority of'))
        heap.changePriority(dat,priority)
    else:
        break


