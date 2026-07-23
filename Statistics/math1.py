#mean / average

# num1,num2,num3,num4,num5 = 40,50,60,70,80
# mean = (num1 + num2 + num3 + num4 + num5) / 5  # This creates a sum in parentheses
# print(mean)


#Deveation (how each element far from mean)
#In statistics, deviation is the difference between a data point and some reference value (usually the mean/average)
# marks = [40,50,60,70,80]
# mean = sum(marks) / len(marks)

# for mark in marks:
#     deviation = mark-mean
#     print(f"{mark} and Deviation ={deviation}")

#Standard Deviation (SD) (sum of squares of deviatons / number of samples)
#square of Deviation 
#-20 = 400
#-10 = 100
#0 =0
#10 =100
#20 =400
#Total = 1000
#SD = 1000/5 = 200.0
import math
# marks = [40,50,60,70,80] 
# mean = sum(marks) / len(marks)
# deviations  = [mark - mean for mark in marks]
# print(deviations)

# square_deviations = [deviation**2 for deviation in deviations]
# print(square_deviations)

# variance = sum(square_deviations) / len(marks)
# print(variance)
# standard_deviation = math.sqrt(variance)
# print(standard_deviation)

# marks = [100,200,300,400,500]
# mean = sum(marks) / len(marks)
# deviations = [mark - mean  for mark in marks]
# squared_deviations = [deviation**2 for deviation in deviations]
# variance = sum(squared_deviations) / len(marks)
# squared_deviations = math.sqrt(variance)
# print(squared_deviations)

#Range (difference between max and min value is called range)

# marks = [40,50,60,70,80]
# range = max(marks) - min(marks)
# print(range)

#Median (Find the middle value after sorting)
# marks = [40,80,70,60,50]
# marks.sort()
# print(marks)
# middle = len(marks) // 2
# print(marks[middle])

# import statistics
# marks = [40,80,70,60,50]
# median = statistics.median(marks)
# print(median)

#Mode - 20
# import statistics
# marks = [10,20,20,30,30,40]
# print(statistics.mode(marks))
# marks = [10, 20, 20, 30, 30, 40]

# # Count frequency of each number
# frequency = {}
# for mark in marks:
#     if mark in frequency:
#         frequency[mark] += 1
#     else:
#         frequency[mark] = 1

# # Find the maximum frequency
# max_count = 0
# mode = None
# for mark, count in frequency.items():
#     if count > max_count:
#         max_count = count
#         mode = mark

# print(f"Mode: {mode}")  # Output: 20 (first occurring mode)

#Determinate (det)

# """
# 2,3
# 1,4

# 8-3=5
#difference between product of diagonals in the matrix
# """

# import numpy as np
# matrix = np.array([[2,3],[1,4]])
# det = np.linalg.det(matrix)
# print(det)

#log means how many times we will raise the power of the number with respect to base is called logarithms



# print(math.log10(100))
# print(math.log2(8))

#correlation
# import numpy as np

# study_hours = [1,2,3,4,5]
# marks = [10,40,60,80,100]
# correlation = np.corrcoef(study_hours,marks)
# print(correlation[0][1])

import pandas as pd
# data = {
#     "study_hours": [1,2,3,4,5],
#     "marks": [10,40,60,80,100]
# }

# df = pd.DataFrame(data)
# print(df.corr())

# data = {
#     "study_hours": [1,2,3,4,5],
#     "marks": [100,80,60,50,40]
# }

# df = pd.DataFrame(data)
# print(df.corr())

#covariance
# import numpy as np
# study_hours = [1,2,3,4,5]
# marks = [20,40,60,80,100]
# covariance = np.cov(study_hours,marks)
# print(covariance[0][1])

import pandas as pd

# data = {
#     "study_hours": [1,2,3,4,5],
#     "marks": [20,40,60,80,100]
# }
# df = pd.DataFrame(data)

# print(df.cov())


# data = {
#     "study_hours": [1,2,3,4,5],
#     "marks": [100,80,60,50,40]
# }

# df = pd.DataFrame(data)

# print(df.cov())


#distrobution

# import numpy as np
# import matplotlib.pyplot as plt

# data = np.random.normal(loc=60,scale=10,size=100)
# plt.hist(data,bins=3)
# plt.title("Normal Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Frequency")
# plt.show()


#Bias

# actual = [80,70,90]
# predicted = [60,50,70]
# bias = (sum(predicted) / len(predicted)) - (sum(actual) / len(actual))
# print(bias)

# actual = [80,70,90]
# predicted = [81,71,91]
# bias = (sum(predicted) / len(predicted)) - (sum(actual) / len(actual))
# print(bias)


#Error  = actual - predicted 

# actual = [80,70,90]
# predicted = [60,50,70]

# for a,p in zip(actual,predicted):
#     error = a - p
#     print(error)


# for any program we call inputs as features and outputs as lables