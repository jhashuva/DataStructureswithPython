from Stack import Stack

stack = Stack()

a ="""
1. PUSH
2. POP
3. TOP
4. EMPTY
5. Max"""

choice = "Yes"

while choice:
    print(a)
    b = int(input('Enter your choice: '))
    if b ==1:
        c = int(input('Enter the element you want to push: '))
        stack.Push(c)
        print(stack.display())

    elif b ==2 :
        if stack.Empty():
            print('Stack is empty')
        else:
            print('Popped element {} from the stack {}'.format(stack.Pop(),stack.display()))

    elif b==3:
        print("The top element in the stack is {}".format(stack.Top()))

    elif b ==4:
        if not stack.Empty():
            print('Stack is not empty')
        else:
            print('Stack is Empty')

    elif b ==5:
        print('Maximum element from the stack is {}'.format(stack.max()))
    else:
        print('Invalid choice')
    choice=input('Do you want to continue? Yes/No')