#tuples
# """
# 1. ordered
# 2.Immutable
# 3.Allows Duplicates
# 4.Faster Compared to lists
# 5.occupies less space 
# 6. it is represented as ()
# 7.it is heterogeneous
# """

#Example-1

# t1=(10,20,30)
# t2= 100,200,300
# t3="Hello"
# print(t1,end=" ")
# print(t2, end=" ")
# print(t3,end = " ")
# print(type(t1),end=" ")
# print(type(t2),end=" ")
# print(type(t3),end=" ")
# t4=(10)
# print(type(t4),end=" ")
# t5=("Hello")
# print(type(t5),end=" ")
# t6=("Vpro",)
# print(type(t6), end=" ")

#Example-2
# import sys
# list1 = [10,20,30,40,50]
# tuple1 = (10,20,30,40,50)
# print(sys.getsizeof(list1))
# print(sys.getsizeof(tuple1))

#Example-3
# tuple1 = (10,20,30,40,50)
# print(tuple1[0])
# print(tuple1[-1])
# print(tuple1[0:3])
# print(tuple1[:2])
# print(tuple1[-3:-5])
# print(tuple1[3:])
# print(tuple1[-3:])
# print(tuple1[::-1])

#Example-4
# tuple1 = (10,20,30,40,50)
# # tuple1[0] = 100 #File "C:\Users\lenovo\OneDrive\Desktop\AgenticAI\tuples-ex.py", line 50, in <module> tuple1[0] = 100
# list1 = list(tuple1)
# list1[0] = 100
# tuple1 = tuple(list1)
# print(tuple1)

#Example-5
# tuple1 = (10,[20,30])
# tuple1[1][0] = 200
# print(tuple1)

#Example-6
# tuple1 = (10,20,30,40,50)
# e1,e2,e3,e4,e5 = tuple1
# print(e1,e2,e3,e4,e5)

# tuple2 = 100,200,300,400,500
# e1,*e2,e3 = tuple2 #100,[200,300,400],500
# x,*y = e2 #200,[300,400]
# *a,b = y #300,[400]
# z,=a #300 #accessing list element from unpacking method
# print(e1,x,z,b,e3)
# print(z)

#Example-7
# def test():
#     return 10,20,30
# e1,*e2 = test()
# *x,y=e2
# a, = x
# print(a,e1,y)


#Example-8
# tuple1 = 10,20,30,40,50,10,20

# print(f"Number of Elements:{len(tuple1)}")
# print(f"Max Element:{max(tuple1)}")
# print(f"Max Element:{min(tuple1)}")
# print(f"Sum of Elements:{sum(tuple1)}")
# print(f"10 repeated:{tuple1.count(10)}")
# print(f"Index of First Occured Element:; {tuple1.index(10)}")

# tuple2 = (10,50,20,40,30)
# print(tuple(sorted(tuple2)))

#Example-9

# tuple1 = (10,20,30,40,50)
# for element in tuple1:
#     print(element)


# for index,value in enumerate(tuple1):
#     print(index,"--->",value)


# tuple2 = ((10,20),(30,40),(50,60))

# for inner_tuple in tuple2:
#     for index,value in enumerate(inner_tuple):
#         print(index,"-->",value)
#         print("--------------------")


#Example-10

# tuple1 = (10,20)
# tuple2 = (30,40)
# tuple3 = tuple1 + tuple2
# print(tuple3)
# tuple4 = tuple3 * 3
# print(tuple4)
# print(10 in tuple4)
# print(10 not in tuple4)
# print(100 not in tuple4)

#Example-11
# d1 = {
#     (10,) : 10
# }

# print(d1)

#Faq1
#Memory locations
#if we modify tuple by without  creating new tuple it will get allocate new memory
# t1 = (10,20,30)
# print(id(t1))
# t1 = t1 + (40,)
# print(id(t1))

#Faq2
# tuple1 = 10,20,30
# tuple2 = 10,20,30
# print(tuple1 == tuple2)
# print(tuple1 is tuple2)
# print(id(tuple1))
# print(id(tuple2))

#Faq2
# tuple1 = 10,20,30
# tuple2 = 10,(20,30)
# print(tuple1 == tuple2)
# print(tuple1 is tuple2)

#Faq3
# for x in range(5):
#     print(x)

# res = [x*x for x in range(5)]

# print(res)

#Faq4
# stds = ("std1","std2")
# marks = (90,100)
# res = tuple(zip(stds,marks))
# print(res)

#Faq5
# marks = (50,55,60,65,75,70)
# average = sum(marks) / len(marks)
# print(average)

# import statistics
# marks = (50, 55, 60, 65, 75, 70)
# average = statistics.mean(marks)
# print(average)  # 62.5

#using loop
# marks = (50, 55, 60, 65, 75, 70)
# total = 0
# for mark in marks:
#     total += mark
# average = total / len(marks)
# print(average)  # 62.5

#using numpy
# import numpy as np
# marks = (50, 55, 60, 65, 75, 70)
# average = np.mean(marks)
# print(average)  # 62.5
