import random
# ---------------------------------------------------------
# question 2
my_list = [(value*2)-1 for value in range(1, 6)]
print("i have created : ")
print(my_list)
# A
print(sorted(my_list, reverse=True))
# B
for num in my_list:
    print(num)
# C
new_list = my_list[:]
i = 0
for num in new_list:
    if (i % 2) == 0:
        new_list[i] = num*5
    i += 1
    print(i)
print(new_list)
# D
new_list.remove(5)
new_list.remove(7)
print(new_list)
# E
new_list.append(int(input("enter number to append ")))
print(new_list)
# F
print("the biggest number is : ")
print(max(new_list))
# G
i = 0
print("the last 3 numbers in the list are : ")
for num in [-1, -2, -3]:
    print(new_list[num])
# H
listX = new_list[0:2]
listY = new_list[3:]
# question 3
# A
Dict = {}
# B
Dict['age'] = 20
Dict['Name'] = input("enter Name : ")
Dict['Specialization'] = input("enter Specialization: ")
print(Dict)
# C
Dict['first food'] = input("enter favorite food : ")
Dict['second food'] = input("enter favorite food : ")
print("the new dictioary is : ")
print(Dict)
# D
print("the keys of the dictionary are : ")
print(Dict.keys())
print(Dict['Name'])
# E
print("{Name} is a professional specialized in {Specialization} and his/her age is {age}. {Name}'s Favorite Foods are {first food} and {second food}".format(**Dict))
# question 4
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
favorite = [1, 4, 3]
for fav in favorite:
    print(color[fav])
# question 5
SQUARE = [(value*2) for value in range(1, 20)]
print("i have created : ")
print(SQUARE)
square1 = SQUARE[:5]
print("i have created : ")
print(square1)
square2 = SQUARE[14:]
print("i have created : ")
print(square2)
subSQUARE = square1 + square2
print("i have created : ")
print(subSQUARE)
# question 6
randomlist = []
size = random.randint(3, 30)
for i in range(0, size):
    n = random.randint(1, 30)
    randomlist.append(n)
print("i have created : ")
print(randomlist)
mx = max(randomlist[0], randomlist[1])
secondmax = min(randomlist[0], randomlist[1])
n = len(randomlist)
for i in range(2, n):
    if randomlist[i] > mx:
        secondmax = mx
        mx = randomlist[i]
    elif randomlist[i] > secondmax and mx != randomlist[i]:
        secondmax = randomlist[i]

print("Second highest number is : ")
print(secondmax)
# question 7
Dict = {}
size = random.randint(3, 30)
for i in range(0, size):
    key = "key" + str(i)
    Dict[key] = random.randint(0, 100)
print("i have created : ")
print(Dict)
all_values = Dict.values()
max_value = max(all_values)
print("max value in Dict is : ")
print(max_value)
# question 8
"""
fromkeys()

The fromkeys() method returns a dictionary with the specified keys and the specified value.
"""
# question 9
colorDict1 = {'R': 'Red', 'G': 'Green', 'W': 'White', 'B': 'Black'}
print("i have created : ")
print(colorDict1)
colorDict2 = {'P': 'Pink', 'Y': 'Yellow'}
print(colorDict2)
colorDict3 = colorDict1.copy()
colorDict3.update(colorDict2)
print("i have created : ")
print(colorDict3)
# question 10
Dict = {0: 'A', 1: 'B', 2: 'C', 4: 'D'}
while True:
    n = input("enter number between 1 and 9 ")
    if (int(n) <= 9 and int(n) >= 0):
        break
result = "false"
for key in Dict:
    if (int(key) == int(n)):
        result = "true"
print(result)
# question 11
Dict = {0: 'A', 1: 'B', 2: 'C', 4: 'D'}
while True:
    n = input("enter number between 1 and 9 ")
    if (str(n) <= "Z" and str(n) >= "A"):
        break
result = "false"
for value in a_dict.values():
    if (str(value) == str(n)):
        result = "true"
print(result)
# question 12
Dict = {0: 10, 1: 20, 2: 12, 4: 7}
for key in Dict:
    Dict[key] *= 5
print("i have created : ")
print(Dict)
