# nums = [1,2,3,4,5]
# for num in nums:
#     print(num, end=" ")


# for num in range(5): #0 included 5 excluded
#     print(num, end=" ")
#=====================================================
# for num in range(2,7):
#     print(num, end=" ")
#=====================================================
# for num in range(0,10,2): #range(inital_value,final_value,incremental_value) printing incremental value
#     print(num, end=" ")
#=====================================================
# for num in range(10,0,-2): #range(inital_value,final_value,-incremental_value) printing reverse incremental value 
#     print(num,end= " ")
#=====================================================
# for num in range(10,0,-1):
#     print(num,end= " ")
#=====================================================
# nums = [10,20,30,40,50]

# for index,element in enumerate(nums):
#     print(f"index is {index} and value is {element}")

#=====================================================
# nums = [100,200,300,400,500]
# for index,element in enumerate(nums,start=1): #index starting with 1
#     print(f"index is {index} and value is {element}")

#reading 2 lists at the same time using zip()method
# stds = ["Std1","Std2","Std3","Std4","Std5"]
# marks = [50,60,70,80,90]

# for std,mark in zip(stds,marks):
#     print(f"student {std} and value is {mark}")
#=====================================================

#finding largest number in given list
# nums = [10,8,6,25,32]
# largest = nums[0]

# for num in nums:
#     if num > largest:
#         largest = num

# print(largest)
#=====================================================
# finding smallest number in given list
# nums = [10,8,6,25,32]
# smallest = nums[0]

# for num in nums:
#     if num < smallest:
#         smallest = num

# print(smallest)
#=====================================================
# """
# ---------------------------------------------
# HOME WORK
# ---------------------------------------------
# """
#=====================================================
#find second largest number
#find second smallest number
#=====================================================
#find even numbers count in the list
# nums = [1,2,3,4,5]
# count = 0
# for num in nums:
#     if num%2 ==0:
#         count += 1
# print(count)
#=====================================================
#find odd numbers count in the list
# nums = [1,2,3,4,5]
# count = 0
# for num in nums:
#     if num%2 !=0:
#         count += 1
# print(count)
#=====================================================
#finding duplicates in given list

# nums = [1,2,3,2,4,5,3]
# duplicates = set()
# for num in nums:
#     if nums.count(num) > 1:
#         duplicates.add(num)

# print(duplicates)
#=====================================================
#reading character by character from the string using for loop
# str = "Python"
# for ch in str:
#     print(ch,end= " ")
#=====================================================
#reversing the string
# str = "Python"
# result = ""
# for ch in str:
#     result = ch + result
# print(result)
#=====================================================
#fibonacci series
# a,b = 0,1

# for _ in range(20):
#     print(a, end=" ")
#     a,b = b, a+b

#=====================================================
# str = "hello"
# count = {}
# for ch in str:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1

# print(count)
# output : {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#=====================================================
#for loop with else block 
# for i in range(5):
#     print(i)
# else:
#     print("done !!")
#=====================================================
# for i in range(1,6):
#     if i ==3:
#         break
#     print(i)

#=====================================================
# for i in range(1,6):
#     if i ==3:
#         continue
#     print(i)
# #output : 1 2 4 5
#=====================================================
# for i in range(1,6):
#     if i ==3:
#         pass
#     print(i)
#=====================================================
# """
# nested loop
# """

# for i in range(3):
#     for j in range(3):
#         print(i,j,sep="->")
#=====================================================
# i=1
# while i<=5:
#     print(i)
#     i += 1
#=====================================================
# i=1
# while i<=5:
#     print(i)
#     i += 1
# else:
#     print("While loop done!!")
#=====================================================
#creating infinite loop

# while True:
#     name = input("Enter Name:")

#     if name == "Quit":
#         break
#     print(name)
#=====================================================
# age = 22
# if age > 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote")
#=====================================================
# age = 22
# if age > 18:
#     print("You are eligible to vote.")
# print("Completed.")
#=====================================================
# age = 22
# citizen = True
# if age>18 and citizen:
#     print("You are eligible to vote.")
#=====================================================
# username = "admin"
# password = 1234
# if username == "admin" or password == 1234:
#     print("Access Granted")
#=====================================================  
# is_logged_in = False
# if not is_logged_in:
#     print("Please Login!!!")
#=====================================================
# age = 25
# salary = 50000
# if age > 18:
#     if salary  > 30000:
#         print("You are eligible for loan.")
#     else:
#         print("Low Salary")
# else:
#     print("You are not eligible for loan.")
#=====================================================
# num = 15
# if num%2 == 0:
#     print("Even Number!!!")
# else:
#     print("Odd Number !!!")
#=====================================================
# num = -10

# if num > 0:
#     print("Positive Number!!!")
# elif num < 0:
#     print("Negative Number !!!!")
# else:
#     print("Zero !!!")    
#=====================================================
#Greatest among the given numbers
# a = 10
# b = 20
# c = 30

# if a >= b and a >=c :
#     print(f"a is greater {a}")
# elif b >= a and b >= c:
#     print(f"b is greater {b}")
# else:
#     print(f"c is greater {c}")

#=====================================================
# name = ""
# if name:
#     print("Not Empty")
# else:
#     print("Empty")
#=====================================================
# nums = [10,20,30,40,50]
# if 30 in nums:
#     print("Available")
#=====================================================
# age = 19

# result = "Major" if age > 18 else "Minor"
# print(result)

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case _:
        print("Invalid Day!!!")


