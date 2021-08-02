import random
import statistics
##############################################################################################
# question 1
Samplelst1 = random.sample(range(0, 30), 10)
print("i have created : ")
print(Samplelst1)
divby3 = []
for num in Samplelst1:
    if num % 3 == 0:
        divby3.append(num)
print("heres a list of numbers that are divisable by 3 : ")
print(divby3)
# question 2
sampletxt = "Welcome to the Computer Applications Lab"
key = input(
    "enter character to scan for in Welcome to the Computer Applications Lab : ")
try:
    result = sampletxt.index(key)
    print("the string is located in index : ")
    print(result)
except ValueError:
    print("it doesnt seem to exist in the string !")
# question 3
list1 = []
for n in range(0, 4):
    inp = input("enter number : ")
    list1.append(inp)

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and \
            mx != list1[i]:
        secondmax = list1[i]

print("Second highest number is : ",
      str(secondmax))
# question 4
numbers = []
while True:
    num = input("enter number, input the literal a to end : ")
    if str(num) == "a":
        break
    elif num == '':
        continue
    try:
        numbers.append(int(num))
    except ValueError:
        print("it looks like you inputed a literal ! only input numbers....")
print("the median of the input list : ")
print(numbers)
print("is : ")
print(statistics.median(numbers))
# question 5
lst1 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
result = {element for element in lst1 if element in lst2}
print("intersection of lst1 and lst2 is : ")
print(result)
c = set()
print("union of lst1 and lst2 is : ")
for element in lst1:
    c.add(element)
for element in lst2:
    c.add(element)
print(c)
# question 7
print("before removing the duplicates : ")
Input = [2, 4, 10, 20, 5, 2, 20, 4]
print(Input)
final_list = []
for num in Input:
    if num not in final_list:
        final_list.append(num)
print("after removing the duplicates : ")
print(final_list)
# question 8
numbers = []
while True:
    num = input("enter number, input the literal a to end : ")
    if str(num) == "a":
        break
    elif num == '':
        continue
    try:
        numbers.append(int(num))
    except ValueError:
        print("Not Valid ! ")
print("your input was : ")
print(numbers)
print("the sum of the inputs is : ")
Sum = sum(numbers)
print(Sum)
print("the average of the list is : ")
print(sum(numbers) / len(numbers))
print("min of the list is : ")
print(min(numbers))
print("max of the list is : ")
print(max(numbers))
# question 9
n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')
