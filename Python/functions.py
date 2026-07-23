# """
#    function
#    -------------
#    particular business logic called as function
#                   (or)
#     set of statements also called as function
#     "def" is the keyword, to represent "empty function"
#     "pass" is the keywordd , to represent "empty function"
# """

# no parameter , no return type
# def addition():
#     num1 = 200
#     num2 = 100
#     res = num1 + num2
#     print(f"addition :: {res}")

# addition()

# no parameters with return type
# def addition():
#     num1 = 200
#     num2 = 100
#     res = num1 + num2
#     return res

# x = addition()
# print(x)


# with parameter no return keyword
# def addition(num1, num2):
#     res = num1 + num2
#     print(f"addition :: {res}")
#     #return res

# addition(200,100)

# with parameter -with return type
# def addition(num1, num2):
#     res = num1 + num2
#     return res

# x = addition(200,100)
# print(x)


#square of a number 

#no parameter - no return type

# def square():
#     num = 2
#     res = num*num
#     print(f"square of the number is :: {res}")

# square()


#no parameter - with return type
# def square():
#     num = 2
#     res = num*num
#     return res

# x = square()
# print(x)

#with parameter - no return type
# def square(num):
#     res = num*num
#     print(f"square of the number is :: {res}")

# square(2)

#with parameter - with return type
# def square(num):
#     res = num*num
#     return res

# x = square(2)
# print(x)

#default parameters
# def test_func(num1=200,num2= 100):
#     res = num1 + num2
#     print(f"addition :: {res}")

# test_func()
# test_func(2000,1000)
# test_func(2000)
# test_func(num2=1000)
# test_func(num1=1)


#normal (regular) with default parameters
# def test_func(param1,param2,param3="Hello"):
#     print(param1,param2,param3)
# # test_func(100,200)
# # test_func(100,200,300)
# test_func(param3="Aggentic AI",param2="Gen AI",param1="Python")

#variable-length arguments
#represented as *
#because of * parameter is converted to tuple
#variable-length is tuple

# def test_func(*param1):
#     print(param1)

#test_func(10,20,30,40,50)
#test_func("Gen AI","Agentic AI")

#functions will allow only 1 variable-length argument
# def test_func(*param1,*param2):
#     pass


# def test_func(param1,param2,param3 = "Hello",param4 = "welcome",param5 = ()):
#     print(param1,param2,param3,param4,param5)

#test_func(100,200) #100 200 Hello welcome ()
#test_func(param3 = 300, param1 = 100, param2 = 200, param4 = 400)
#test_func(param1=1,param2=2,param3=3,param4=4,param5 = (5,6,7,8,9,10))

# def test_func(param1,param2,param3 = "Hello",param4 = "welcome",*param5 ):
#     print(param1,param2,param3,param4,param5)

#test_func(100,200) #100 200 Hello welcome ()
#test_func(param3 = 300, param1 = 100, param2 = 200, param4 = 400)
#test_func(param1=1,param2=2,param3=3,param4=4,param5 = (5,6,7,8,9,10)) #TypeError: test_func() got an unexpected keyword argument 'param5'. Did you mean 'param1'?


#keyword arguments
#it is represented as **
#keyword argumets would store in the form of dictonary
#used to store the values in the form of a key-value pairs  (this is considered as other form of the dicronary)
# def test_func(**param1):
#     print(param1)

# test_func(name="VPro",sub= "Gen AI")

# def test_func(param1,param2="Hello",*param3,**param4):
#     print(param1,param2,param3,param4)
#     print(type(param3))
#     print(type(param4))
# test_func(100,200,300,400,500,num1=600,num2=700)
#test_func(100,)

#normal parameters
#default parameters
#variable-length 
#keyword-length arguments


# def test_func(*subjects):
#     for sub in subjects:
#         print(sub) #to print each element in new line
#        # print(sub,end= " ") # to print all elements in single line

# test_func("GENAI","Agentic AI","RAG","MCP","MCP CLient")

#lambda - anonymous functions 

# res = lambda num1: num1 * num1
# print(res(10))

# x = lambda num1,num2: num1+num2
# print(x(200,100))

"""
to manipulate all elements in python we use map() 
example :
1. 2. 3. 4. 5
    x100
100 200 300 400 500
--------------------------------------------------
to apply condition we have filter()
1000 2000 3000 4000 5000
    > 3000
    4000 5000
---------------------------------------------------
1 2 3 4 5

sum of the given numbers 
15

we have reduce()

-----------------------------------------------------

"""

#addition using lambda
# addition = lambda num1,num2: num1 + num2

# print(addition(200,100))

#cube of a given number using lambda
# cube_number = lambda num1: num1*num1*num1
# print(cube_number(5))


# even or odd using lambda

# x = lambda num1: "Even" if num1%2 ==0 else "Odd"

# print(x(2))

#multiplication using lambda
# x = lambda  num1,num2,num3 : num1* num2 * num3
# print(x(10,20,30))

# subs = ["GenAI","AgenticAI","Quantum","RAG"]

#sort based on length
#sorted - predefined function used to sort the lists
#Key, used to customize the sorted function

# res = sorted(subs,key=lambda x:len(x), reverse=True)

# print(res)

#manipulate all elements using map() 
#store result to list
# print(list(map(lambda x :x*x, [1,2,3,4,5,6])))

#input [1,2,3,4,5] ---> expected output [0.5,1,1.5,2,2.5]

# print(list(map(lambda x:x/2 , [1,2,3,4,5])))

# print(tuple(map(lambda x:x/2 , (1,2,3,4,5))))

#to evaluate conditions using python we will use filter() 

#print even numbers
# print(list(filter(lambda x:x%2 ==0 ,[1,2,3,4,5,6,7,8,9,10])))

#print odd numbers

# print(list(filter(lambda x:x%2 !=0 ,[1,2,3,4,5,6,7,8,9,10])))


#to find sum of all elements in list or tuple we use reduce()

# from functools import reduce

# print(reduce(lambda num1,num2: num1+num2,[1,2,3,4,5]))

from functools import reduce

# print(reduce(lambda num1, num2: num1+num2,list(filter(lambda num1:num1<900,list(map(lambda num1:num1*num1,[10,20,30,40,50]))))))

#print(reduce(lambda num1,num2: num1+num2 ,list(filter( lambda num1:num1>900,list(map(lambda num1:num1*num1,[10,20,30,40,50]))))))

#[100, 400, 900, 1600, 2500]


#[1,2,3,4,5] - [1000,2000,3000,4000,5000] --> [3000,4000,5000]

#print(reduce(lambda num1,num2:num1+num2 ,list(filter(lambda num1:num1>2000,map(lambda num1:num1*1000,[1,2,3,4,5])))))

#sort based on salary
# emps = [("Emp1",50000),("Emp2",30000),("Emp3",510000)]

# emps.sort(key = lambda emp:emp[1])
# print(emps)

# res = sorted(emps,key=lambda x:x[1])
# print(res)


#largest number in a given list

# largest_number = lambda num1,num2 : "num1 is largest"  if num1 > num2 else "num2 is largest "

# print(largest_number(55,25))


# largest_number = lambda num1,num2,num3 : "num1 is largest"  if num1 > num2 & num1 > num3  else ( "num2 is largest " if num2 > num3 else "num3 is the largest") 
# print(largest_number(55,36,77))

#last character of the string 
# str = "Hello"
# print(str[-1])
# print(str[4])

