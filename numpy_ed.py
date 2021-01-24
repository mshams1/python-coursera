# Numpy is the fundamental package for numeric computing with Python. 
# It provides powerful ways to create, store, and/or manipulate data, 
# which makes it able to seamlessly and speedily integrate with a wide variety of databases. 
# This is also the foundation that Pandas is built on, which is a high-performance data-centric package
#  that we will learn later in the course.

# In this lecture, we will talk about creating array with
# certain data types, manipulating array, selecting elements 
# from arrays, and loading dataset into array. Such functions
# are useful for manipulating data and understanding the
# functionalities of other common Python data packages.

import numpy as np

################
################
################
# Arrays

# Arrays are displayed as a list or list of lists
# When creating an array, we pass in a list as an argument in numpy array

# If we pass in a list of lists in numpy array, we create a multi-dimensional array, for instance, a matrix
# integers & floats are also accepted in numpy arrays

## Array Creation 

a = np.array([1, 2, 3])
b = np.array([[1,2,3],[4,5,6]]) # b.shape gives the length of each dimension of b --> (2,3)
c = np.array([2.2, 5, 1.1])
d = np.zeros((2,3)) # all zeros
e = np.random.rand(2,3)
f = np.arange(10, 50, 2) # every even number from ten (inclusive) to fifty


## Array Operations

a = np.array([10,20,30,40])
b = np.array([1, 2, 3,4])
farenheit = np.array([0,-10,-5,-15,0])
A = np.array([[1,1],[0,1]]) # A.shape gives (2,2)
B = np.array([[2,0],[3,4]])

c = a-b
d = a*b
celcius = (farenheit - 31) * (5/9)
e = celcius > -20 # array([ True, False, False, False,  True])
f = celcius%2 == 0
G = A*B # elementwise product
H = A@B # matrix product
i = np.arange(1,16,1).reshape(3,5) # from 1 to 15 in 3*g dim

print(celsius.sum())
print(celsius.max())
print(celsius.min())
print(celsius.mean())

#################################
#################################
#################################
# Indexing, Slicing and Iterating 

## indexing (integer indexing & Boolean indexing)
a = np.array([1,3,5,7])
a[2]

a = np.array([[1,2], [3, 4], [5, 6]])
a[1,1]

print(a > 5)  # This returns a boolean array showing that if the value at the corresponding index is greater than 5
print(a[a>5]) # returns 6

## Slicing ( to create a sub-array based on the original array)
a = np.array([0,1,2,3,4,5])
print(a[:3])

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a[:2, 1:3])

# caution: a slice of an array is a view into the same data / modifying the sub array will consequently modify the original array

############################
############################
############################
# Trying Numpy with datasets EXAMPLE

# To load a dataset in Numpy, we can use the genfromtxt() function. We can specify data file name, delimiter (which is optional but often used), and number of rows to skip if we have a header row, hence it is 1 here

# The wine data fields include: fixed acidity, volatile aciditycitric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxidedensity, pH, sulphates, alcohol, quality

wines = np.genfromtxt("datasets/winequality-red.csv", delimiter=";", skip_header=1)

wines[:, 0] # all rows combined but only the first column from them

wines[:, 0:1] # # But if we wanted the same values but wanted to preserve that they sit in their own rows we would write

wines[:,-1].mean() # mean of column quality

# the graduate school admissions data fields inclde: GRE score, TOEFL score, university rating, GPA, having research experience or not, and a chance of admission

graduate_admission = np.genfromtxt('datasets/Admission_Predict.csv', dtype=None, delimiter=',', skip_header=1,
                                   names=('Serial No','GRE Score', 'TOEFL Score', 'University Rating', 'SOP',
                                          'LOR','CGPA','Research', 'Chance of Admit'))

graduate_admission.shape # the resulting array is actually a one-dimensional array with 400 tuples

graduate_admission['CGPA'][0:5] #  the CGPA column and only the first five values

len(graduate_admission[graduate_admission['Research'] == 1]) # how many students have had research experience 




