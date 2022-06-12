def myFunction(n):
    myList=[]
    nineteen=0
    five=0
    for i in range(n):
        myList.append(int(input()))
    print(myList)

    for i in range(n):
       if myList[i]==19:
            nineteen=nineteen+1
    for i in range(n):
       if myList[i]==5:
            five=five+1
    
    if nineteen==2 and five>=3:
        return True
    else:
        return False

n=int(input("Enter the range:"))
print(myFunction(n))