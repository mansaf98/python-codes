import numpy as np
##############################################################################################
# question 1
print("i have created : ")
x = np.array([[-1, -1, -1, -1, -1], [1, 5, 5, 5, 1],
              [1, 5, 20, 5, 1], [1, 5, 5, 5, 1], [1, 1, 1, 1, 1]])
print(x)
# question 2
print("i have created : ")
x = np.random.randint(20, 40+1, (5, 5))
print(x)
# q2a
xmin = x.min()
print("Minimum Value is :")
print(xmin)
# q2b
xmean = np.mean(x)
print("mean for each column is :")
print(xmean)
# q2c
xbigger = x[x > 30]
print("there are {} numbers that are bigger than 30 and these are : ".format(xbigger.size))
print(xbigger)
# q2d
xsmaller = x[x < 30]
print("there are {} numbers that are smaller than 30 and these are : ".format(
    xsmaller.size))
print(xsmaller)
# q2e
x = np.append(x, np.random.randint(0, 30+1, (5, 1)))
print("i have appended 5 values to each row, new array is : ")
print(x)
# q2f
print("top 10 elements in the array are : ")
print(x[np.argsort(x)[-10:]])
# question 3
x = np.random.randint(0, 100+1, (1, 5))
print("i have created array x : ")
print(x)
y = np.random.randint(0, 100+1, (1, 5))
print("i have created array y : ")
print(y)
mask = np.invert(np.isin(x, y))
print("here are the elements that are unique to array x : ")
print(x[mask])
# question 4
grades = np.genfromtxt(
    r"C:\Users\yazan\OneDrive\Desktop\summer_2021\python\lab6\Grades.txt", dtype=int)
print("uploaded the grades : ")
print(grades)
# q4a
max_grade = np.amax(grades, axis=0).astype(np.float64)
print("highest grade scored at the final exam is : ")
print(max_grade[2])
# q4b
total = np.sum(grades, axis=1)
grades85 = total[total >= 85]
print("a number of {} students achieved a grade of 85 % and more their grades are : ".format(grades85.size))
print(grades85)
# q4c
mean = np.mean(grades, axis=0)
print("the mean for the assignments is {} , and midterm {} , and final {}".format(
    mean[0], mean[1], mean[2]))
std = np.std(grades, axis=0)
print("the standard deviation for the assignments is {} , and midterm {} , and final {}".format(
    std[0], std[1], std[2]))
# q4d
Dict = {'assignment': std[0], 'mid': std[1], 'final': std[2]}
max_key = max(Dict, key=Dict.get)
print("the assesment tool with highest standard deviation is :")
print(max_key)
# q4e
print("{} students had a maximum score in the assignment ".format(
    np.argwhere(grades[..., 0] == 20).size))
# question 6
"""
Clip (limit) the values in an array.
numpy.clip(a, a_min, a_max, out=None, **kwargs)
When a_min is greater than a_max, clip returns an array in which all values are equal to a_max
"""
print("clip function example : ")
a = np.arange(10)
print(a)
print("after running np.clip(a, 1, 8) all values above 8 where clipped to 8")
print(np.clip(a, 1, 8))
print("after running np.clip(a, 8, 1) all values above 1 where clipped to 1")
print(np.clip(a, 8, 1))
