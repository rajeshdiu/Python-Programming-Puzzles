from ast import Store
from itertools import count
from traceback import print_tb
def myFunction(n):
    myList=[]
    nineteen=0
    five=0
    for i in range(n):
        myList.append(int(input()))
    print(myList)

    list_len=len(myList)

    count=0

    Store=[]
    for i in range(n):
        if myList[i]==myList[4]:
            Store.append(myList[i])
    print(Store)
    for i in range(n):
        if myList[i]==Store[0]:
            count=count+1
    print(count)

    if list_len==8 and count==3:
        return True
    else:
        return False

n=int(input("Enter the range:"))
print(myFunction(n))