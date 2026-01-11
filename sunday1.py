# class and objects
# class student:
#     def __init__(self,name=None,course=None):
#         self.name=name
#         self.course=course
#     def show(self):
#         print(f"{self.name} is a student of {self.course}")

# s1=student()
# s1.name="Aadesh Shukla"
# s1.course="Cse"
# s1.show()
# s2=student("Vaishu","cse")
# s2.show()
#__________________________________________________________
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node("Apple")
# node2=Node("Banan")
# node3=Node("Grapes")
# node1.next=node2
# node2.next=node3
# node3.next=None
# def print_list(head):
#     current=head
#     while current is not None:
#         print(current.data,end="->")
#         current=current.next 
#     print("None")
# print_list(node1) 
# node1.next.data="blueberry" 
# print_list(node1)
#_________________________________________________________
class student:
    def __init__(self,name=None,course=None):
        self.name=name
        self.course=course
    def show(self):
        print(f"{self.name} is a student of {self.course}")
    def update_name(self,new_name):
        self.name=new_name 
    def update_course(self,new_course):
        self.course=new_course


s1=student("Aadesh","CSE")
s1.show()
s1.update_name("Aadesh Shukla")
s1.update_course("AIML")
s1.show()
           
            
