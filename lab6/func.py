import numpy as np
##############################################################################################
data = np.genfromtxt(
    r"C:\Users\yazan\OneDrive\Desktop\summer_2021\python\lab6\Data.txt", dtype=int, delimiter=",")
print(data)
# q5a
K = input("enter K to find top K numbers in the data : ")
print("the top {} numbers in data :".format(int(K)))
print(data[np.argsort(data)[-int(K):]])
# q5b
print("the first occurency of any number greater than 90 is in data[{}]".format(
    np.argmax(data > 90)))
# q5c
print("the array is after removing duplicates :")
print(np.unique(data))
# q5d
print("most occuring grade is {}".format(
    np.unique(data)[np.where(np.unique(data, return_counts=True)[1] == np.amax(np.unique(data, return_counts=True)[1]))]))
