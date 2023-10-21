from ast import Num
from collections import UserList
from itertools import count
import re
import string
from time import sleep
from turtle import update

from numpy import append, intp, number, product


Print = print
printf = print
Int = int
"""
myTuple = (2345,"tufts", 1.0, 40)
print (myTuple)  
print(len(myTuple))

userIn1 = int(input("Put in an int"))
userIn2 = int(input("Put in an int"))
userIn3 =int(input("Put in an int"))
userIn4 =int(input("Put in an int"))
myTuple=(userIn1,userIn2,userIn3,userIn4)
print(myTuple.count(2))

valueTuple = (2202, 45, 10, 567)
user = int(input("what number you looking for?"))
if user in valueTuple:
    print("item found")
else:
    print("item not found")

difTuple = ("To", 1, 92, "Good", 9.1)
saTuple = (1.2, 3.1, 5.9)
if type(difTuple) == float:
    print("all items are type of",type(difTuple))
else:
    print("The items are not of the same type")

myList = [1,5,2,3,8]
print(myList)
myList.sort(reverse = True)
print(myList)

NameList = []
for name in range(5):
    NameList.append(input("NAME?\n"))
print(NameList)

NumberList =[]
for ask in range(5):
    NumberList.append(int(input("Give me a number:\n")))

i = 0
while i < len(NumberList):
    if NumberList[i] % 2 == 0:
        NumberList.pop(i)
    else:
        i += 1
print(NumberList)
"""
"""
res = []
for num in NumberList:
    if num % 2 != 0:
        res.append(num)
print(res)
"""
"""
myList = [0,9,8,10,6]
maxIdx = 0
for i in range(len(myList)):
    if myList[i] > myList[maxIdx]:
        maxIdx = i
print(maxIdx, myList[maxIdx])

listtest = [1,9,0,8]
for i in listtest:
    print(i,end="")

mySet = {0,1,2,"The entity"}
print(len(mySet))

mySet = {2,5,3,7,8,9}
user_input = int(input("enter a number:\n"))

if user_input in mySet:
    print("number is in set")
else:
    print("number is not in set")
#
infSet = {"talk","laugh", "speak"}
while "quit" not in infSet:
    print(infSet)
    infSet.add(input("put in a pharse or quit" + " \n"))
#
huskSet = { "words",1,0,2}

myDict = {0:10, 1:20}
myDict.update({2:30})
print(myDict)

Dic1 = {1:10, 2:20}
Dic2 = {3:30, 4:40}
Dic3 = {5:50, 6:60}
SingDict = {}

SingDict.update(Dic1)
SingDict.update(Dic2)
SingDict.update(Dic3)
print(SingDict)
#
mySum = 0
myProduct = 1
for key, value in SingDict.items():
    mySum += key
    myProduct *= value
print(mySum,myProduct)

#takes user's name and age and then returns age after code.
def user(name,age):
    print("hello,",name)
    if age >= 25:
        print("you are an Adult")
    else:
        print("you are not an Adult")
    return(age)
name = input("what is your name\n")
age = int(input("what is your age\n"))
age = user(name,age)
#
def add_2(num1,num2):
    prbint("adding", num1,"to",num2)
    sum = num1 + num2
    return(sum)
def subtract_2(num1,num2):
    print("Subtracting", num1,"from",num2)
    difference = num2 - num1
    return(difference)
def multiply_2(num1,num2):
    print("multiplying", num1,"by",num2)
    product = num1*num2
    return(product)
def divide_2(num1,num2):
    print("dividing", num1,"by",num2)
    Quotient = num1/num2
    return(Quotient)
nume1= int(input("what is num1\n"))
nume2= int(input("what is num2\n"))
sum = add_2(nume1,nume2)
sleep(0.9)
print("The sum of",nume1,"and",nume2,"is", sum)
sleep(0.9)
difference = subtract_2(nume1,nume2)
sleep(0.9)
print("The difference of",nume1,"and",nume2,"is", difference)
sleep(0.9)
product = multiply_2(nume1,nume2)
sleep(0.9)
print("The product of",nume1,"and",nume2,"is", product)
sleep(0.9)
Quotient = divide_2(nume1,nume2)
sleep(0.9)
print("The Quotient of",nume1,"and",nume2,"is", Quotient)
#
"""