import BinarySearchTree as BST

bst = BST.BinarySeaarchTree()

a = """
1. Insert
2. Search
3. Delete
4. In-order
5. Pre-Order
6. Post-Order
7. Level-Order"""

while True:
    print(a)
    choice = int(input('Enter your choice: '))
    if choice ==1:
        dat = input('Enter the data you want to insert: ')
        bst.insert(dat)

    elif choice == 2:
        dat = input('Enter the element you want to search: ')
        if bst.search(dat):
            print(f'{dat} is in the tree')
        else:
            print(f'{dat} is not in the tree')
    elif choice == 3:
        dat = input('Enter the element to delete: ')
        bst.remove(dat)
    elif choice == 4:
        print('In-order traversal: ')
        bst.in_order(bst.root)
    elif choice == 5:
        print('Pre-order traversal: ')
        bst.pre_order(bst.root)
    elif choice == 6:
        print('Post-order traversal: ')
        bst.post_order(bst.root)
    elif choice == 7:
        print('Level order traversal:')
        bst.levelOrderTraversal(bst.root)
    else:
        break