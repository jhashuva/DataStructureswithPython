from Queue import Queue
q = Queue()

a = """
1. Enqueue
2. Dequeue
3. Empty
"""

choice = 'Yes'

while choice:
    print(a)
    inp = int(input("Enter correct choice: "))
    if inp == 1 :
        b = input('Enter the element to insert in the queue: ')
        q.enqueue(b)
        print('Queue is {}'.format(q.display()))
    elif inp == 2:
        q.dequeue()
        print('Queue is {}'.format(q.display()))
    elif inp ==3:
        if q.empty():
            print('Queue is empty')
        else:
            print('Queue is not empty')
    else:
        print('Invalid choice')
    choice = input('Do you want to continue ? Yes/No')

