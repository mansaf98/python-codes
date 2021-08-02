##############################################################################################
def question_1():
    numbers = []
    i = 0
    while True:
        num = input("enter number ")
        if num == '':
            continue
        try:
            numbers.append(int(num))
            i = i+1
        except ValueError:
            print("Wrong ")
        if i == 5:
            break
    print("your numbers are : ")
    print(numbers)
    print("the max number is : ")
    print(max(numbers))
    return


def question_2():
    while True:
        try:
            number = int(input("Enter the integer number : "))
            break
        except ValueError:
            print("dont input string ")
    revs_number = 0
    while (number > 0):
        remainder = number % 10
        revs_number = (revs_number * 10) + remainder
        number = number // 10
    print("The reverse number is : ")
    print(revs_number)
    return


def question_3():
    while True:
        try:
            num = int(input("Enter number to check if prime or not : "))
            break
        except ValueError:
            print("dont input string ")
    if (num == 1):
        print("number is not prime")
        return
    elif (num == 2):
        print("number is prime")
        return
    else:
        for x in range(2, num):
            if(num % x == 0):
                print("number is not prime")
                return
        print("number is prime")
        return


def question_4(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    print("intersection of the 2 lists {} and {} is:".format(lst1, lst2))
    print(lst3)
    return


def question_5(n):
    return lambda a, b, c: (a+b+c)/n


def question_6(lst):
    print("list before removing duplicates :")
    print(lst)
    lst = list(set(lst))
    print("list after removing duplicates :")
    print(lst)
    return


def question_7(filename):
    infile = open(filename, 'r')
    students = {}
    for line in infile:
        line = line.strip()
        phrase = line.split(' ', 2)
        students.update({phrase[0] + " " + phrase[1]: phrase[2]})
    infile.close()
    students.pop('first_name Last_name')
    print("the students are :")
    print(students)
    print("the student with the minimum grades is : ")
    print(min(students, key=students.get))
    for name, score in students.items():
        students[name] = int(score) + 3
        if int(students[name]) > 100:
            students[name] = 100
    print("added 3 marks to all new students, new grades are : ")
    print(students)
    for name, score in students.items():
        if int(students[name]) < 40:
            students[name] = 40
    average = 0
    print("all students with grades under 40 now have a score of 40 : ")
    print(students)
    for name, score in students.items():
        average += int(students[name])
    print("average of the class is : ")
    print(average/len(students))
    print("top 3 students are : ")
    print(sorted(students, key=students.get, reverse=True)[:3])
    return


def question_8(filename):
    print("words that start with A and are longer than 7 characters : ")
    with open(filename, "r") as a_file:
        for line in a_file:
            for word in line.split():
                if((word.startswith("A")) and (len(word) > 7)):
                    print(word)
    return


##############################################################################################
# question 1
question_1()
# question 2
question_2()
# question 3
question_3()
# question 4
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
question_4(lst1, lst2)
# question 5
average = question_5(3)
print(average(3, 2, 1))
# question 6
lst = [1, 3, 5, 6, 3, 5, 6, 1]
question_6(lst)
# question 7
question_7(r"C:\Users\yazan\OneDrive\Desktop\Data.txt")
# question 8
question_8(r"C:\Users\yazan\OneDrive\Desktop\lorem.txt")
