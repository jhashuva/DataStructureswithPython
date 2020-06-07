import HashTable as HT
ht = HT.HashTable()

a = """
1. Insret Key, value
2. Get the key"""

while True:
    print(a)
    choice = int(input('Enter your choice: '))
    if choice == 1:
        key = input('Enter the key: ')
        value = input('Enter the value: ')
        ht.put(key,value)
    elif choice ==2:
        key = input('Enter the key to retrive the value: ')
        #if ht.get(key):
        print(f'{ht.get(key)}')
        #else:
    elif choice==3:
        print(ht.slots)
    else:
        print('Invalid choice')
        break
