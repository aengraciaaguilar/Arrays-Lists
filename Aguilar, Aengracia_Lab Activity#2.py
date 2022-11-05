# Laboratory Activity #2
# Name: Aguilar, Aengracia
# Year and Section: BSCOE 2-2 

import random
 
aarand_list=[]
n=10
for i in range(n):
    aarand_list.append(random.randint(3,9))
print("Array: ",aarand_list)

print("Menu:")
print("1 -> Add an element")
print("2 -> Insert an element")
print("3 -> Modify an element")
print("4 -> Delete an element")
print("5 -> Arrange in ascending order")
print("6 -> Arrange in descending order")

x=int(input("What do you want to do? (1-6): "))
if x==1:
    print("Add an element")
    a=int(input("Enter element: "))
    aarand_list.append(a)
    print("The element has been added")
elif x==2:
    print("Insert an element")
    a1=int(input("Enter index: "))
    a2=int(input("Enter element: "))
    aarand_list.insert(a1,a2)
    print("The element has been inserted")
elif x==3:
    print("Modify an element")
    a1=int(input("Enter index: "))
    a2=int(input("Enter element: "))
    
    aarand_list[a1]=a2
    print("The element has been modified")
elif x==4:
    print("Delete an element")
    a11=int(input("Enter the index you want to delete: "))
    del aarand_list[a11]
    print("The element has been deleted")
elif x==5:
    print("Arrange in ascending order")
    aarand_list.sort()   
    print("The list has been sorted")
elif x==6:
    print("Arrange in descending order")
    aarand_list.sort(reverse=True)  
    print("The list has been sorted in descending order")
else:
    print("Invalid choice")
print("This is the new array: ",aarand_list)
    

