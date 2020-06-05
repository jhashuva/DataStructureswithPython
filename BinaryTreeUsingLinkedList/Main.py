from BinaryTree import BinaryTree
bt = BinaryTree()

a="""
1. Insert at root
2. Insert at left
3. Insert at right
4. Height of the node
5. Size of the tree
6. Pre-order Traversal
7. In-Order Traversal
8. Post-order Traversal
9. Level-order Traversal
"""

choice = 'Yes'

while choice:
    print(a)
    inp = int(input('Enter valid choice: '))
    if inp ==1:
        b= input('Enter the element you want to insert at root: ')
        bt.set_root(b)
    elif inp ==2:
        ele = input('Enter the element you want to insert the data at left: ')
        dat = input("Enter the data you want to insert: ")
        bt.insert_left(ele,dat)
    elif inp==3:
        ele = input('Enter the element you want to insert the data at right: ')
        dat = input("Enter the data you want to insert: ")
        bt.insert_right(ele,dat)
    elif inp==4:
        ele = input('Enter the node to calculate the height ')
        node = bt.find(bt.get_root(),ele)
        print('Height of tree from the node {} is {}'.format(ele,bt.height(node)))
    elif inp==5:
        print('Size of the tree is {}'.format(bt.size(bt.get_root())))
    elif inp==6:
        print('Pre-order traversal:')
        bt.preOrderTraversal(bt.get_root())
    elif inp==7:
        print('In-order Traversal')
        bt.inOrderTraversal(bt.get_root())
    elif inp==8:
        print('Post-order traversal: ')
        bt.postOrderTraversal(bt.get_root())
    elif inp==9:
        print('Level-order traversal:')
        bt.levelTraversal(bt.get_root())
    else:
        print('Invalid choice')
    choice = input('Do you want to continue? Yes/No ')