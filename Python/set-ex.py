# """
# Sets are unordered - Elements in a set have no defined order and cannot be accessed by position.

# Sets are mutable - You can add or remove elements from a set after creation.

# Sets do not allow duplicates - Each element in a set must be unique; duplicate values are automatically eliminated.

# Sets do not support indexing - Individual elements cannot be accessed using index positions like set[0].

# Sets allow heterogeneous elements - A set can contain elements of different data types (e.g., integers, strings, floats, booleans).

# Sets can be created using curly braces {} or the set() constructor - Empty sets must be created using set() since {} creates an empty dictionary.

# Sets do not support slicing operations - You cannot extract a subset of elements using slicing syntax like set[1:3].

# Sets support searching operations - You can efficiently check if an element exists in a set using the in operator.

# Sets work on the hashing technique - Elements are stored and accessed using hash values, which makes membership testing and element operations very fast (O(1) average time complexity).


# """

#Example-1

# s1 = { }
# print(type(s1))

# s2 = set()
# print(type(s2))

#Example-2

# s1 = {10,20,10,20,30}
# print(s1)

# list1 = [10,20,10,20,30]
# s2 = set(list1)
# print(s2)

# tuple1 = (10,10,20,30,20)
# s3 = set(tuple1)
# print(s3)

#Example-3
# s1 = {10,20,30}
# print(s1[0]) #File "C:\Users\lenovo\OneDrive\Desktop\AgenticAI\set-ex.py", line 46, in <module> print(s1[0]) ~~^^^TypeError: 'set' object is not subscriptable

#Example - 4
# s1 = {1,2,3,4}
# s1.add(4)
# list1 = [5,6,7,8,8]
# s1.update(list1) # adding list to set
# print(s1)

# tuple1 =(9,10)
# s1.update(tuple1) #adding tuple to set

# print(s1)

# # s1.remove(10) # remove particular element , if element not available it will throw error
# s1.discard(10) # it will try to remove the element if it is present , if element not present it will not throw error

# s1.pop() #it will remove random element
# s1.clear() # it will clear entire element
# print(s1)

#Example-5
# s1 = {1,2,3}
# s2 = {3,4,5}
# print(s1.union(s2))
# print(s1 | s2 )
# print(s1.intersection(s2))
# print(s1 & s2 )

# print(s1.difference(s2))
# print(s1-s2)

# print(s1.symmetric_difference(s2)) #common elements will be deleted
# print(s1^s2) ##common elements will be deleted

#Example -6
# s1 = {10,20,30,40,50}
# print(20 in s1)
# print(20 not in s1)

#Example-7
# s1 = {10,20,30,40,50}
# for element in s1:
#     print(element)

# s2 = {{10,20},{30,40}}

# for inner_set in s2: #File "C:\Users\lenovo\OneDrive\Desktop\AgenticAI\set-ex.py", line 91, in <module>  s2 = {{10,20},{30,40}} ^^^^^^^^^^^^^^^^^ TypeError: cannot use 'set' as a set element (unhashable type: 'set')
#     print(inner_set)


# res = {x*x for x in range(5)}
# print(res)

#Example - 9

#creating freezed set
# s1 = frozenset([1,2])
# print(type(s1))

#FAQ1
# s1 = set("Hello")
# print(s1)

#FAQ2
# s1 = {1,True,1.0}
# print(s1)

#FAQ3
# s1 = {10,20,50,40,30}
# print(s1)
# print(len(s1))
# print(max(s1))
# print(min(s1))
# print(sum(s1))
# print(sorted(s1))

