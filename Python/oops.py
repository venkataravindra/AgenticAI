"""
class
---------------------
 - collection of "variables and functions" called as "class"
 - "class"  is the keywordd used to delcare the class
 -  "pass" is the keyword used to create empty class

 - "constructors" are used to initilize the "instance members"
 - "__init__()" called as constructor in python
 - self is the keywordd, used to recognize the instance members

 Inheritance:
    getting the data from parent class to child class called as Inheritance
    1) single level
    2) multi level
    3) multiple inheritance
    4) hybrid inheritance

"""
#static initialization

# class Test:
#     def __init__(self):
#         self.num1 = 200
#         self.num2 = 100

# obj1 = Test()
# obj1.num1 = 2000


# obj2 = Test()
# print(obj2.num1)


#dynamic initilization
# class Test:
#     def __init__(self,param1,param2):
#         self.num1 = param1
#         self.num2 = param2

# obj1 = Test(200,100)
# res = obj1.num1 + obj1.num2
# print(f"Addition : {res}")
# print(f"num1 {obj1.num1} and num2 is {obj1.num2}")


# direct or static initilization
# class Test:
#     def __init__(self):
#         pass

# obj1 = Test()
# obj1.x = 200

# print(obj1.x)


# class Test:
#     def __init__(self):
#         pass

#     def add(self):
#         num1 = 2
#         res = num1 ** num1
#         print(res)

# obj1 = Test()
# obj1.add()



# class Test:
#     #no parameter no return type
#     def square1(self):
#         x = 10
#         res = x * x
#         print(f"square1 : {res}")
#     #with parameter no return type
#     def square2(self,num1):
#         res = num1 * num1
#         print(f"Square2 : {res}")
    
#     #no parameter with return type
#     def square3(self):
#         x = 10
#         res = x * x
#         return res
#     #with parameter with return type
#     def square4(self,param1):
#         res = param1 * param1
#         return res

# obj1 = Test()
# obj1.square1()
# obj1.square2(2)
# output = obj1.square3()
# print(output)

# output1 = obj1.square4(5)
# print(output1)


"""
-------------------------------------------------
inheritance examples
-------------------------------------------------
"""

#single inheritance

# class Parent:
#     def __init__(self):
#         self.msg = "Hello"

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.subject = "Agentic AI"

# obj1 = Child()
# print(obj1.msg)
# print(obj1.subject)

# obj2 = Parent()
# print(obj2.msg)
#print(obj2.sub) #AttributeError: 'Parent' object has no attribute 'sub'


# class Parent():
#     def __init__(self,param1):
#         self.msg = param1

# class Child(Parent):
#     def __init__(self, param1,param2):
#         super().__init__(param1)
#         self.sub = param2

# obj1 = Child("Hello","Agentic AI")
# print(obj1.msg, end=" ")
# print(obj1.sub)

# class Parent:
#     def test_func1(self):
#         print("Hello")
# class Child(Parent):
#     pass

# obj1 = Child()
# obj1.test_func1()

"""
---------------------------------------------
multi level inheritance
---------------------------------------------
"""

# class Parent:
#     def __init__(self):
#         self.num1 = 300
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.num2 = 200
# class SubChild(Child):
#     def __init__(self):
#         super().__init__()
#         self.num3 = 100

# obj1 = SubChild()
# print(obj1.num1 + obj1.num2 + obj1.num3)


#pass the data through super keyword

# class Parent:
#     def __init__(self,param1):
#         self.param1 = param1
# class Child(Parent):
#     def __init__(self, param1,param2):
#         super().__init__(param1)
#         self.param2 = param2

# class SubChild(Child):
#     def __init__(self, param1, param2,param3):
#         super().__init__(param1, param2)
#         self.param3 = param3

# obj1 = SubChild("Hello","Ravindra","Learn Agentic AI")
# print(obj1.param1,end=" ")
# print(obj1.param2,end=" ")
# print(obj1.param3,end=" ") 



# class Parent:
  
#     def test_func1(self):
#         print("Hello!!")

# class Child(Parent):
#     def test_func2(self,sub):
#         return sub

# class SubChild(Child):
#     def test_func3():
#         print("VPro edu Tech") 
#         return "VPro edu Tech"       

# obj2 = SubChild()
# print(obj2.test_func1())
# print(obj2.test_func2("Welcome to"))
# print(obj2.test_func3())


# class Parent:
#     def test_func1(self):
#         print("Hello!!")
#         #return "Hello!!"  # Return something to print

# class Child(Parent):
#     def test_func2(self, sub):
#         return sub

# class SubChild(Child):
#     def test_func3(self):
#         print("VPro edu Tech")
#         #return "VPro edu Tech"  

# obj2 = SubChild()
# print(obj2.test_func1())       
# print(obj2.test_func2("Welcome to"))  
# print(obj2.test_func3())       


"""
--------------------------------------------
Multiple inheritance
--------------------------------------------
"""

# class Parent1:
#     def __init__(self):
#         self.num1 = 200

# class Parent2:
#     def __init__(self):
#         self.num2 = 100

# class Child(Parent1 , Parent2):
#     def __init__(self):
#         Parent1.__init__(self)
#         Parent2.__init__(self)

# obj = Child()
# print(obj.num1)
# print(f"Addition :{obj.num1 + obj.num2}")

# class Parent1:
#     def __init__(self):
#         self.num1 = 200
# class Parent2:
#     def __init__(self):
#         self.num1 = 2000
# class Child(Parent1,Parent2):
#     def __init__(self):
#         Parent1.__init__(self)
#         Parent2.__init__(self)
#         # self.num1 = 20000

# obj = Child()
# print(obj.num1)

# class Parent1:
#     def __init__(self,num1):
#         self.num1 = num1

# class Parent2:
#     def __init__(self,num1):
#         self.num1 = num1
# class Child(Parent1,Parent2):
#     def __init__(self, param1,param2,param3):
#         Parent2.__init__(self,param2)
#         Parent1.__init__(self,param1)
#         self.num1 = param3

# obj = Child(1,10,100)
# print(obj.num1)
        
    
# class Parent1:
#     def test_func1(self):
#         num1 = 100
#         return num1
# class Parent2:
#     def test_func2(self):
#         num1 = 1000
#         return num1
# class Child(Parent1,Parent2):
#     def test_func3(self):
#         num1 = 10000
#         return num1

# obj = Child()
# print(obj.test_func1())
# print(obj.test_func2())
# print(obj.test_func3())


# class Parent:
#     def __init__(self):
#         self.x = 1000
# class Child1(Parent):
#     def __init__(self):
#         super().__init__()
#         self.y = 2000
# class Child2(Parent):
#     def __init__(self):
#         super().__init__()
#         self.y = 20000

# obj1 = Child1()
# print(obj1.x,obj1.y)

# obj2 = Child2()
# print(obj2.x,obj2.y)

#multi level inheritance
# class Parent:
#     def test_func1(self):
#         num1 = 2000
#         return num1
# class Child1(Parent):
#     def test_func2(self):
#         num1 = 20000
#         return num1

    
# class Child2(Parent):
#     def test_func3(self):
#         num1 = 20000000
#         return num1

# obj1 = Child1()
# print(obj1.test_func1(),obj1.test_func2())

# obj2 = Child2()
# print(obj2.test_func1(),obj2.test_func3())

#Hybrid inheritance

# class Parent:
#     def __init__(self):
#         self.num1 = 100
   
# class Child1(Parent):
#    def __init__(self):
#        super().__init__()
#        self.num1 = 1000
# class Child2(Parent):
#     def __init__(self):
#         super().__init__()
#         self.num1 = 10000
# class SubChild(Child1,Child2):
#     def __init__(self):
#         Child1.__init__(self)
#         Child2.__init__(self)
#         self.num1 = 100000

# obj = SubChild()
# print(obj.num1)


# class Test:
#     name = "JNTU"

# obj1 = Test()
# obj2 = Test()
# print(obj1.name)
# print(obj2.name)

# class Test:
#     name = "JNTU"
#     def __init__(self):
#         self.name = "STD1"

# obj = Test()
# print(obj.name)

# class Test:
#     name = "JNTU"
#     def __init__(self):
#         pass
#         # self.name = "STD1"

# obj = Test()
# print(obj.name)

#adding instance variables during runtime

# class Test:
#     name = "JNTU"

# obj = Test()
# obj.name = "KLU"
# print(obj.name)


#modifying class level variables
# class Test:
#     name = "JNTU"

# Test.name = "KLU"
# print(Test.name)

# class Test:
#     name = "JNTU"

#     @classmethod
#     def test_func(cls):
#         cls.name = "KLU"

# Test.test_func()
# print(Test.name)



"""
method over riding
polymorphism
child class method overrides parent class method this is called method overriding
"""

# class Parent:
#     def dbfun(self):
#         return "Oracle DB Conn Soon..."
    
# class Child(Parent):
#     def dbfun(self):
#         return "Vector DB Conn Soon..."

# obj = Child()
# print(obj.dbfun())



"""
private variables
"__"used to declare private variables
unable to access with the help of objects
unalbe to access in child classes
able to access with in the class
"""

# class Test:
#     def __init__(self):
#         self.__x = 200

# obj = Test()
# print(obj.__x) #AttributeError: 'Test' object has no attribute '__x'


# class Parent:
#     def __init__(self):
#         self.__x = 200
# class Child(Parent):
#     pass

# obj = Child()
# print(obj.__x) #AttributeError: 'Child' object has no attribute '__x'

# class Test:
#     def __init__(self):
#         self.__x = 100
#     def setX(self):
#        self.__x = 1000
#     def getX(self):
#         return self.__x

# obj = Test()
# print(obj.getX())

# class Test:
#     def __init__(self):
#         self.__salary = 10000
#     def __getSalary(self):
#         return self.__salary
#     def calculate_pf(self):
#         return self.__salary*0.1

# test = Test()
# print(test.calculate_pf())

# class MyClass:
#     def _helper(self):
#         print("Internal helper method")

# obj = MyClass()
# obj._helper()

"""
protected
able to access with the help of objects
accessable in child classes also
"""

# class Parent:
#     def __init__(self):
#         self._x = 100
# class Child(Parent):
#     pass
# obj = Child()
# print(obj._x)

"""
to override hashcodes we use def __str__(self) method
"""

# class Test:
#     pass
#     # def __str__(self):
#     #     return "Hello World!!"

# obj = Test()
# print(obj)

# class Test:
#     def __str__(self):
#         return "Hello World!!"

# obj = Test()
# print(obj)

"""
abstract method and its implementation
""" 
# from abc import ABC,abstractmethod

# class Test(ABC):
#     @abstractmethod
#     def start_business(self):
#         pass
# class Child(Test):
#     def start_business(self):
#         return "Start Edu Tech / Software Solutions"

# obj = Child()
# print(obj.start_business())

"""
utility methods
"""

# class Calculator:
#     @staticmethod
#     def add(x,y):
#         return x+y

# print(Calculator.add(20,30))

# constructor overloading is not supported in python
# class Test:
#     def __init__(self):
#         self.x = 100
#     def __init__(self, name):
#         self.name = name

# obj = Test("Ravinda")
# print(obj.name)

# python will not support method overloading 

# class Test:
#     def test(self,x):
#         print(x)
#     def test(self,x,y):
#         print(x,y)

# obj = Test()
# obj.test(10,20)

#as below mentioned we can achieve overloading with the help of variable length arguments

# class Test:
#     def test(self,*param):
#         print(param)

# obj = Test()
# obj.test(10,20,30,40,50)
