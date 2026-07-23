import numpy as np

#declaration of 1D array
# arr1 = np.array([10,20,30,40,50,60])

# 
# print(arr1)
# print(arr1.ndim) #printing dimentions of array
# print(arr1.shape) 
# print(arr1.size)
# print(arr1.dtype)

#declaration of 2D array

# arr2 = np.array([[10,20,30],
#                  [40,50,60],
#                  [70,80,90]])

# print(arr2)
# print(arr2.ndim)
# print(arr2.shape)
# print(arr2.size)
# print(arr2.dtype)

#create 0's array
# arr1 = np.zeros((3,4))
# print(arr1)

#create 1's array
# arr2 = np.ones((2,5))
# print(arr2)
#printing values between the range using arrays
# arr1 = np.arange(10,21)
# print(arr1)
#stepping values by 2 numbers
# arr2 = np.arange(10,21,2)
# print(arr2)

#linear space 
#here 0 to 100 divided by 5 spaces
# arr1 = np.linspace(0,100,5)
# print(arr1)

#converting 1d to 2d
# arr1 = np.arange(1,13)
# print(arr1.shape)
# print(arr1)
# #reshaping the array
# arr2 = arr1.reshape(3,4)
# print(arr2)

#converting 2d to 1d
# arr1 = np.array([[1,2],[3,4]])
# arr2 = arr1.flatten()
# print(arr2)

#note for converting 1d to n-d we need to use reshape()
#for converting n-d to 1d we need to use flatten()

#1-d array
#applying conditions to array
# arr1 = np.array([25000,50000,75000,100000])
# arr2 = arr1[arr1 > 50000]
# print(arr2)

#accessing indexes or fancy indexing - accessing morethan 1 index at a time
# marks = np.array([55,60,65,75,85,95])
# print(marks[0]) #accessing single index
# print(marks[[0,2,4]]) # accessing multiple index

#Broad casting example
#if it not numpy we need to manipulate using loop 
# salary = np.array([10000,20000,30000,40000,50000])
# new_salaries = salary + 5000
# print(new_salaries)

#matrix addition

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr3 = arr1 + arr2
# print(arr3)

# arr4 = np.array([[1,2],
#                 [3,4]])
# arr5 = np.array([[5,6],
#                 [7,8]])

# arr6 = arr4 + arr5
# print(arr6)


#matrix multiplication

# arr1 = np.array([[1,2],
#                 [3,4]])
# arr2 = np.array([[5,6],
#                 [7,8]])

# arr3 = np.matmul(arr1,arr2)
# print(arr3)

# marks = np.array([55,60,65,75,85,95])

# print(marks.sum())
# print(marks.max())
# print(marks.min())
# print(marks.mean())

# arr1 = np.array([[1,2],
#                  [3,4]])

# print(arr1.sum(axis=0)) #column wise sum if axis =0
# print(arr1.sum(axis=1)) # row wise sum if axis =1

#Apply condition over arrays using numpy
# marks = np.array([55,60,65,75,85,95])

# result = np.where(marks>60 , "pass","fail")
# print(result)

#sorting an array
# arr1 = np.array([10,50,20,40,30])
# arr2 = np.sort(arr1)
# print(arr2)

#printing random numbers
# np.random.seed(10) #to generate same set of numbers we will use this line
# arr1 = np.random.randint(1,100,15) #without above we will generate different random numbers
# print(arr1)

# arr1 = np.array([1,2,3])
# arr2 = arr1
# arr1[0] = 100
# print(arr2)

# arr1 = np.array([1,2,3])
# # arr2 = arr1
# arr2 = arr1.copy()
# arr1[0] = 100
# print(arr2)


# arr1 = np.array([10,50,20,40,30])
# print(arr1.argmax()) #will print maximum of 0th index among the list of numbers
# print(arr1.argmin())  #will print minimum of 0th index among the list of numbers


"""
---------------------------------------------------------------------------
interview questions on numpy
---------------------------------------------------------------------------
"""

#find the salaries greater than 50000

# salaries =  np.array([10000,30000,20000,50000,90000,15000])
# highest_salaries = salaries[salaries > 50000]
# print(highest_salaries)

#replace negative values with 0

# profits = np.array([100,-50,30,-10,1000,-90])
# new_profits = np.where(profits<0,0,profits)
# print(new_profits)

#find the duplicates
# arr1 = np.array([10,20,30,10,20,30])
# unique,counts = np.unique(arr1,return_counts=True)
# print(unique,counts)

#reverse an array
# arr1 = np.array([10,20,30,40,50])
# new_array = arr1[::-1]
# print(new_array)

#find top 3 elements

# arr1 = np.array([10,20,40,30,50,60])
# top_elements = np.sort(arr1)[-3:]
# print(top_elements)

#concat arrays we use concatenate method in numpy

# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])
# new_arr = np.concatenate((arr1,arr2))
# print(new_arr)

#split an array
#array should be regular array (it should be even sized) else we will get an error if we use split function
# arr1 = np.arange(12)
# parts= np.split(arr1,3)
# print(parts)

#stack arrays vertically

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr3 = np.vstack((arr1,arr2))
# print(arr3)


#stack arrays horizantally

# arr1 = np.array([[1],[2],[3]])
# arr2 = np.array([[4],[5],[6]])

# #to merge horizantally we need 2D arrays

# arr3 = np.hstack((arr1,arr2))

# print(arr3)


#Identity matrix 

# arr1 = np.identity(4)
# print(arr1)


#display diagonal values

# arr1 = np.array([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]])

# arr2 = np.diag(arr1)
# print(arr2)


#dot product

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# res = np.dot(arr1,arr2)
# print(res) #(1*4) + (2*5) + (3*6)

# arr1 = np.array([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]])
# arr2 = np.array([[4,5,6],
#                  [1,2,3],
#                  [9,8,7]])

# res = np.dot(arr1,arr2)

# print(res)

#normalization

# marks = np.array([50,60,70,80,90])

# normalization = (marks - marks.min()) / (marks.max() - marks.min())
# print(normalization)

#count even numbers
# arr1 = np.array([10,25,20,25,30,35])

# even_numbers = arr1[arr1%2 == 0] # print even numbers in an array

# print(even_numbers)

# x = np.count_nonzero(arr1 % 2  ==0) # print count of even numbers in an array
# print(x)


# arr1 = np.arange(1,10)
# print(arr1)

# arr2 = arr1.reshape(3,3)
# arr1[0] = 100
# print(arr2)

# arr2[2][2] = 900

# print(arr1)

