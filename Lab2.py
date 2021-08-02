import math

#---------------------------------------------------------------------------------------------
#question 1 - 6

X = 5
Y = 10
Z = 19.5
W = ((X/(Y)**2) + (Z**(1/3)))
print("if X = {} ".format(X) + "and Y = {} ".format(Y) + "and Z = {} ".format(Z) + "then W = {} ".format(W))

#---------------------------------------------------------------------------------------------
#question 7

rad = input("enter radius of circle ")
print("the area of the circle is: " + str(math.pi * (int(rad)**2)))

#---------------------------------------------------------------------------------------------
#question 8-9

first_name = input("enter first name ")
last_name = input("enter last name ")
age = input("enter age ")
name = first_name + " " + last_name
My_info = ("My name is {} and my age is {} ".format(name, age)).title()
print(My_info)
print(My_info[0:(11+len(first_name))])
print(My_info[29:-1])

#---------------------------------------------------------------------------------------------
#question 10

A = int(input("enter first number for comparission "))
B = int(input("enter second number for comparission "))
if(A >= B):
    print("True")
else:
    print("False")

#---------------------------------------------------------------------------------------------
#question 11

S = "Python is Interpreted Languagee"
S = S[0:-1]
S = S+"#"
print(S)

#---------------------------------------------------------------------------------------------
#question 12

"""
method formats the specified values and insert them inside the string's placeholder that is defined using curly brackets {}.
example on format function: 
print ("my name is {name}".format(name = yazan))
output:
my name is yazan
refrence: https://www.w3schools.com/python/ref_string_format.asp
"""