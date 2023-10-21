"""
def int_to_bin(num):
    intNum = num
    print(bin(intNum)[2:])

num = int(input("Num "))
int_to_bin(num)
#
def d_string(phrase : str) -> str:
    new_list = []
    doubled_string = ""
    for i in range(len(phrase)):
        new_list.append(phrase[i])
    for i in range(len(new_list)):
        new_list[i] = new_list[i] * 2
    for i in new_list:
        doubled_string += i
    print(doubled_string)

sting = input("input string\n")
d_string(sting)
#
def isPalindrome(string):
	return string == string[::-1]

s = input("give a number:\n")
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
#

def reverse_number(num):
    c_num = str(num)
    digits_list = []
    rc_num = ""
    for i in range(len(c_num)):
        digits_list.append(c_num[i])
    digits_list.reverse()
    for i in digits_list:
        rc_num = rc_num + " " + i
    print(rc_num)
        

number = int(input("Input an inteager:\n"))
reverse_number(number)
#
def make_dollars(dollars):
    dollar = []
    num_hundos = dollars // 100
    dollars = dollars - (num_hundos * 100)
    num_fifties = dollars // 50
    dollars -= (num_fifties * 50)
    num_twenties = dollars // 20
    dollars -= (num_twenties * 20)
    num_tens = dollars // 10
    dollars -= (num_tens * 100)
    num_fives = dollars // 5
    dollars -= (num_fives * 5)
    num_ones = dollars
    dollar.append(num_hundos)
    dollar.append(num_fifties)
    dollar.append(num_twenties)
    dollar.append(num_tens)
    dollar.append(num_fives)
    dollar.append(num_ones)
    return dollar

amounts = int(input("Enter the number of dollars:\n"))
dollars = make_dollars(amounts)
print("\nhundreds:", dollars[0], "\nfifties:", dollars[1],"\ntwenties:", dollars[2],"\ntens:", dollars[3],"\nfives:",dollars[4],"\nones",dollars[5])

n = int(input("num:\n"))
count = 0
while n > 1:
    if count ==1000:
        exit()
    print(n)
    if n % 2 == 0:
        n = n//2
        print(n)
    else:
        n = n * 3 + 1
        print(n)
    count += 1
"""
#
#

user_int = int(input("how long:\n"))

def find_files(user):
    files = []
    i = 0
    while i < user:
        f = int(input("add file size:\n"))
        files.append(f)
        i += 1
    for i in range(len(files)):
        print("\n",files[i],"kb")
    return files

# this func is pointless
def num_of_sub_files(file : list):
    file_count = 0
    for i in range(len(file)):
        file_count += 1
    print(file_count,"is the amount of files that need to be compressed")
    return file_count

def min_cost_of_compress(file : list, file_count : int) -> int:
    add_list =[]
    cost_list =[]
    for j in range(file_count):
        for i in range(1):
            m = min(file)
            ind = file.index(m)
            fm = file.pop(ind)
            add_list.append(fm)
        cost = sum(add_list)
        cost_list.append(cost)
    print(cost_list)


f = find_files(user_int)
fc = num_of_sub_files(f)
nc = min_cost_of_compress(f,fc)


