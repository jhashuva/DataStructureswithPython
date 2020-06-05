import LinkedList as ll
#from LinkedList import LinkedList as ll
ll = ll.LinkedList()
z = """
1.Push Front
2. Top Front
3. Pop Front
4.Push Back
 5. Top Back
 6. Pop Back
 7. Find
 8. Add After
 9. Empty
 10. Number of nodes in the list"""

x=True
while x:
    print(z)
    choice = int(input("Enter valid choice: "))
    if choice==1:
        d=input('Enter the data to push front: ')
        ll.PushFront(d)
        print("After adding {} , The number of nodes in the list is {}".format(d,ll.display()))
    elif choice==2:
        print("The top front element is {}".format(ll.TopFront()))
    elif choice==3:
        ll.PopFront()
        print("After Pop Front number of nodes in the list is {}".format(d, ll.display()))
    elif choice==4:
        d=input('Enter the data to push back: ')
        ll.PushBack(d)
        print("After adding {} number of nodes in the list is {}".format(d, ll.display()))
    elif choice==5:
        print("The top back element is {}".format(ll.TopBack()))

    elif choice==6:
        ll.PopBack()
        print("After Pop Back {},  the list is {}".format(d, ll.display()))
    elif choice==7:
        d=input("Enter the element to find: ")
        a= ll.Find(d)
        if a:
            print("The element {} is present in the list".format(d))
        else:
            print("The element {} is not present in the list".format(d))
    elif choice==8:
        n=input("Enter the node you want insert it after: ")
        d=input("Enter the element you want to insert after {}: ".format(n))
        if ll.Find(n):
            ll.AddAfter(n,d)
            print("Successfully Inserted element {} after the node {}".format(d,n))
        else:
            print("There is no node {} in the list so I cant do it".format(n))
    elif choice==9:
        if ll.Empty():
            print("Yes the list is empty")
        else:
            print("NO list is not empty")
    elif choice==10:
        print("The number of nodes in the list is {}".format(ll.count()))
    else:
        x= False
