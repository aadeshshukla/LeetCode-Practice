 #if you want to take any input

# data=input("enter items separated by spaces: ").split()
# print("You entered:", data) 
#_______________________________________________________
 #if you want to take integer input

# data1=list(map(int,input("enter numbers separated by spaces: ").split()))
# print("You entered numbers:", data1)
#_______________________________________________________
#if you want to take controlled input one by one

# n=int(input("enter number of items you want to input: "))
# data2=[]
# for i in range(n):
#     item=input(f"enter item {i+1}: ")
#     data2.append(item)
# print("You entered the following items:")
# print(data2)
#_______________________________________________________
#if you want to take controlled integer input one by one
# n=int(input("enter number of items you want to input: "))
# data3=[]
# for i in range(n):
#     item=int(input(f"enter number {i+1}: "))
#     data3.append(item)
# print("You entered the following numbers:")
# print(data3)
#_______________________________________________________
# n=int(input("enter number of items you want to input: "))
# data3=[]
# for i in range(n):
#     item=int(input(f"enter number {i+1}: "))
#     data3.append(item)
# print("You entered the following numbers:")
# print(data3)
# data3.sort()
# print("sorted list:",data3)
# even=[]
# odd=[]
# for i in range(n):
#     if data3[i]%2==0:
#         even.append(data3[i])
#     else:
#         odd.append(data3[i])

# print(even)
# print(odd)
#_______________________________________________________
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")
   
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

ll=LinkedList()
n=int(input("enter number of items you want to input: "))
for i in range(n):
    item=int(input(f"enter number {i+1}: "))
    ll.append(item)
ll.display()

            

