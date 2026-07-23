#List
# list is the ordered
#it is representd with []
#list is mutable
# it allows heterogeneous elements
#index starts from 0

# list1 = [10,20,30,40,50]
# print(list1[0])
# print(list1[-5])
# print(list1[0:3])
# print(list1[-3:-1])
# print(list1[3:])
# print(list1[:2])
# print(list1[::-1])
# print(list1[::-2])
# print(list1[::-3])

# import sys
# list2 = [10,"Hello",True,10.1,None]
# list2[0] = 1000
# print(sys.getsizeof(list2))
# print(list2)

#tuple
#it is ordered
#tuple is immutable
#tuple is represented as ()
#index also starts from 0
#tuples occupies less memory when compared to lists
#tuple operations are faster compared to lists
#tuple uses hashtables intenally 
#tuple will allow heterogenious

# import sys
# list1 = [10,20,30,40,50]
# tuple1 = (10,20,30,40,50) 
# print(sys.getsizeof(list1))
# print(sys.getsizeof(tuple1))
# print(type(list1))
# print(id(list1))

# tuple1 = (10,20,30,40,50) 
# tuple1[2] = 3000 #TypeError: 'tuple' object does not support item assignment
# print(tuple1)

#tuple to list conversion
# tuple1 = (10,20,30,40,50)
# list1 = list(tuple1)
# #list to tuple
# list1[0] = 1000
# tuple2 = tuple(list1)
# print(tuple2)


#dictonary
#key - value pairs
#keys are immutable
#values are mutable
#{}


# d1 = {
#     "name" : "vpro",
#     "sub" : "Agentic AI"
# }

# print(d1)
# print(d1.keys())
# print(d1.values())
# print(d1.items())


# d1 = {
#     "name" : "Agentic"
# }
# d1["name"] = "Agentic AI"
# d1["f_sub"] = "Quantum Computing"
# print(d1)

# d1 = {}
# d1["key1"] = 100
# d1["key2"] = 200
# d1["key3"] = 300
# d1["key1"] = 1000
# d1.pop("key2")
# d1.popitem()
# print(d1)


#set
#never allows duplicates
#set is represented with {}
#

# s1 = {10,20,30,10,20,30}
# print(s1)

# s2 = set([10,20,30,10,20,30])
# print(s2)

# s3 = set((10,20,30,10,20,30))
# print(s3)

#None (empty / no value)
# x = None
# print(x)
# print(type(x))
\
#%s - string
#%d - number
#%f - float

# name = "VPro"
# print("I am the founder of %s" % name)

# sub = "Agentic AI"
# ver = 2
# print("Current Trending Sub is %s and Respective Version is %d" %(sub,ver))

# fever = 97.5
# print("Fever = %f" %fever)
# print("Fever = %.2f" %fever)

# name = "VPro"
# year = 2025
# print("name is {} and established in {}".format(name,year))
# print("name is {1} and established in {0}".format(year,name))

# name = "VPro"
# year = 2025

# print(f"Name is {name} and established in {year}")

# num1 = 100
# num2 = 0x123ABC

# print(num2)

# num3 = 0o123
# print(num3)
# num4 = 0b1010
# print(num4)



#for styled text
# from rich import print

# print("[red]Hello[/red]")
# print("[bold green]VPro[/bold green]")

