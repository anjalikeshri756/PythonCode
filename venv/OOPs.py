# class Person:
#     name="Anjali"
#     designation="Developer"
#     address="Barhi"
#
#     def info(self):
#         print(f"{self.name} is a {self.designation} and lives at {self.address}")
#
# a=Person()
# a.info()


# #constructor
# class Planet:
#     def __init__(self,name,location,spin):
#         self.name=name
#         self.location = location
#         self.spin = spin
#     def rotate(self):
#         print(f"planet {self.name} is located in {self.location} and takes around {self.spin} spins per minute")
#
# p=Planet("Mercury","universe",1234)
# p.rotate()

#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return (math.pi)*self.radius*self.radius
#
# c=Circle(2)
# ar=c.area()
# print(ar)

#Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def age(self):
        today=date.today()
        age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        return age

p=Person("anjali","dncj",date(1962, 7, 12))
age=p.age()
print(age)
