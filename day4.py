# x = 10/ x = object
# if(x<20 and (x+y)<z)/ x,y,z = object
#0
#lst = object
#tesdtdict = object
#Lst, a, [z:"name"], [[1,3,7],[4,5]], [1,3,7],[4,5]
#
"""
class Myclass:
    x=5
o = Myclass()
print(o.x+2)
#
class Myclass:
    x = 10
o = Myclass()
print("The value of x is", o.x )
#

import email

class Contact:
    name=""
    phone=[]
    email=""
def func(obj):
    obj.name = input("enter name:\n")
    n =""
    while len(n)!=10:
        n = input("Enter nukmber:\n")
    obj.phone = n.split()
    obj.email = input("enter email:\n")

obj = Contact()
func(obj)
print(obj.name)
print(obj.phone)
print(obj.email)
#Finish this one, question 3 of classes
class Student:
    Name=""
    Roll_number=[]
    score={}
    attendnce =[]

def collector(student):
    student.Name = input("Student name:\n")
# reference
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age


n = input("not working")
a = int(input("age?"))

p1 = People(n,a)
p2 = People("John",37)
print(p1.name)
print(p2.age)
#
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
       area = 3.14 * self.radius**2
       print("area of the circle is",area)
    def circumference(self):
        circumference = 2 * 3.14 * self.radius
        print("circumference of the circle is", circumference)

num = Circle(5)
num.circumference()
num.area()
#

import math
from turtle import update
class triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def hypotenuse(self):
        return ((self.base ** 2) + (self.height ** 2))**0.5
         
    def area(self):
        return (self.base * self.height) * 0.5

def convertor(obj):
    Dict = {"area":obj.area(),"Hypotenuse":obj.hypotenuse()}
    print(Dict)

T = triangle(3,4)
convertor(T)
"""



    





    



