from ctypes.wintypes import HMODULE
from tkinter import CENTER, S
from typing import List
"""
def most_common_int(array:List[int]) -> int:
    countDict = {}

    for val in array:
        if val in countDict:
            countDict[val] += 1
        else:
            countDict[val] = 1
    
    print(countDict)
    # (element, occurrances)
    mostCommonPair = (array[0], countDict.get(array[0]))
    for elem, count in countDict.items():
        if count > mostCommonPair[1]:
            mostCommonPair = (elem, count)

    print(mostCommonPair)

    return mostCommonPair[0] 

myList = [1,2,3,4,5,6,6,7,8,8,9,1,2,1,1]
results = most_common_int(myList)
print(results)
#


def make_change(cents):
    num_quarters = cents // 25
    cents = cents - (num_quarters * 25)
    num_dimes = cents // 10
    cents -= num_dimes * 10
    num_nickels = cents // 5
    cents -= num_nickels * 5
    num_penny = cents
    cents -= num_penny
    
    return num_quarters,num_dimes,num_nickels,num_penny
cents = int(input("Enter the number of cents: "))
print(make_change(cents)) 
#
print("For", cents, "cents, it takes")
print("-" * 20)
num_quarters = cents // 25
cents = cents - (num_quarters * 25)
print("The number of quarters is:", num_quarters)
num_dimes = cents // 10
cents -= num_dimes * 10
print("The number of dimes is:", num_dimes)
num_nickels = cents // 5
cents -= num_nickels * 5
print("The number of nickels is:", num_nickels)
num_penny = cents
cents -= num_penny
print("The number of pennies is:", num_penny)
#
"""
#1
"""
def find_dup_elem(array):
    unique = set()
    for val in array:
        if val not in unique:
            unique.add(val)
        else:
            return val
    return -1

myList = [1,2,3,2,3]
print(find_dup_elem(myList))
#


mySum = 0
myArray = [
    [1,2,3,4],
    [5,6,7,8],
]

for i in range(len(myArray)):
    for j in range(len(myArray[i])):
        mySum = mySum + myArray[i][j]
print(mySum)
#
myProduct = 0
myProduct2 = 0
myArray = [
    [1,2],
    [3,4],
]
holdArray = []
for i in range(len(myArray)):
    for j in range(len(myArray[i])):
        myProduct =  myArray[1][0] * myArray[0][0]
        myProduct2 = myArray[0][1] * myArray[1][1]
holdArray.append(myProduct)
holdArray.append(myProduct2)
print(myArray,"->",holdArray)
#
"""
def leap_year():
    pass
