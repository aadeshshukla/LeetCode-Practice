# class student:
#     def __init__(self,name=None,course=None):
#         self.name=name
#         self.course=course
#     def show(self):
#         print(f"{self.name} is a student of {self.course}")
#     def update(self,newname=None,newcourse=None):
#         self.name=newname
#         self.course=newcourse
#     def add_more_details(self,age,city):
#         self.age=age
#         self.city=city

# s1=student()
# s1.name="Aadesh Shukla"
# s1.course="Cse"
# s1.show()
# s2=student("Vaishu","cse")
# s2.show()
# s2.update("mausam","AIML")
# s2.show()
# s2.show()
# s1.add_more_details(20,"Lucknow")
# s1.show()

# 
class player:
    def __init__(self,name=None,team=None):
        self.name=name
        self.team=team
    def show(self):
        print(f"{self.name} is a player of {self.team}")
    def update(self,newname=None,newteam=None):
        self.name=newname
        self.team=newteam
    def add_more_details(self,age,city):
        self.age=age
        self.city=city

p1=player()
p1.name="Virat Kohli"   
p1.team="India"
p1.show()
p2=player("Rohit","India")
p2.show()
p2.update("Rohit Sharma","India")
p2.show()

# what more we can do with class and object
# inheritance
class cricket(player):
    def __init__(self,name=None,team=None,role=None):
        super().__init__(name,team)
        self.role=role
    def show(self):
        print(f"{self.name} is a {self.role} of {self.team}")   
        
c1=cricket()
c1.name="Sachin"
c1.team="India"
c1.role="Batsman"
c1.show()
c2=cricket("Rohit","India","Batsman")
c2.show()

# error:Traceback (most recent call last):
#   File "D:\Users\91939\Desktop\LeetCode-practice\class.py", line 65, in <module>
#     c2.update("RohitSharma","India","Batsman")
# TypeError: player.update() takes from 1 to 3 positional arguments but 4 were given
c2.update("RohitSharma","India")
c2.show()