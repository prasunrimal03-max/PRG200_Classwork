class Student:
  college="Havard"
  def __init__(self,name,age):
    self.name= name
    self.age = age
s1 = Student("Alice",20)
s2 = Student("Bob",22)
print(s1.name,s1.college)
print(s2.name,s2.college)