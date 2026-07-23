import pandas as pd

#version 
#printing pandas version
# print(pd.__version__)

#list to tabular data convertion
# list1= [10,20,30,40,50]
# data=pd.Series(list1)
# print(data)

#customized index
# list1= [10,20,30,40,50]
# data=pd.Series(list1,index = ["a","b","c","d","e"])
# print(data)

#mapping indexes with actual list using Series()
# marks = [50,60,70,80,90,100]
# students = ["std1","std2","std3","std4","std5","std6"]
# data = pd.Series(marks,index = students)
# print(data)

#data frame demonstration
# data = {
#     "Name": ["Emp1","Emp2","Emp3","Emp4","Emp5"],
#     "Age" : [25,30,35,40,45],
#     "Salary": [50000,60000,70000,80000,90000]
#         }
# df = pd.DataFrame(data,index=["1","2","3","4","5"])
# print(df)


#reading csv file
df = pd.read_csv("employees.csv")
# print(df)
# print first 5 rows
# print(df.head())
# print(df.tail())
# print(df.shape)

# print(df.columns) # to know columns names
#print(df.info())
#print(df.describe()) #mean ,max,min,std
#print(df["EmpID"])
# print(df[["EmpID","Name","Salary"]])
# print(df[df["Salary"]>50000])
#print(df[(df["Salary"]>50000) & (df["Age"]>23)])

#adding new column
# df["Performance Bonus"] = df["Salary"] * 0.10
# print(df.info())
#updating value in a column
# df.loc[0,"Salary"] = 80000
# print(df.head())
#print(df.loc[0])
#print(df.iloc[11])
# print(df.shape)
# df.drop("Bonus",axis=1,inplace=True)
# print(df.shape)


df = pd.read_csv("employees_null.csv")
# print(df)

#print(df.isnull()) #to know null values
#to know count of null values
# print(df.isnull().sum())

# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# print(df["Salary"])
# df["City"] = df["City"].fillna("UnKnown")
# print(df["City"])


#if row contain any null value delete that row
# clean_df =df.dropna()
# print(clean_df)
# print(df.shape)
# cleaned_df = df.dropna(subset=["PerformanceRating"])
# print(cleaned_df)
# print(df.shape)

#operations on employees object
employees = {
"EmpID": [101,102,103,104,105],
"Name": ["Sam","John","David","Priya","Anjali"],
"Department": ["IT","HR","Finance","IT","Sales"],
"Salary": [55000,70000,45000,90000,60000],
"Experience": [2,5,1,8,4]
}


df = pd.DataFrame(employees)
#print(df)
# df1 =  df.sort_values("Salary") #sorting based on salary
# df2 =  df.sort_values("Salary", ascending=False) #sorting based on salary on descending order
# print(df1)
# print(df2)
#df1 = df.sort_values(by = ['Department','Salary'],ascending=[True,False]) #sorting based on department and salary
#print(df1)

#df1 = df.sort_values("Salary", ascending=False).head(3) #sorting based on salary and displaying first 3 records
#print(df1)
#finding sum of salary as per department
#df1 = df.groupby("Department")["Salary"].sum()
# df1 = df.groupby("Department")["Salary"].mean()
# df2 = df.groupby("Department")["Salary"].max()
# df3 = df.groupby("Department")["Salary"].max()
# df4 = df.shape[0]
# print(df1)
# print(df2)
# print(df3)
# print(f"count of employees is ::{df4}")

#finding "min","max","mean","sum","count" in one short we will use "agg()" function
# df1 = df.groupby("Department")["Salary"].agg(["min","max","mean","sum","count"])
# print(df1)

# df1 = df["Salary"].rank()
# print(df1)

# df1 = pd.DataFrame(
#     {
#         "EmpId":[101,102,103],
#         "Name":["Emp1","Emp2","Emp3"]
#     }
# )


# df2 = pd.DataFrame(
#     {
#         "EmpId":[101,102,103],
#         "Salary":[50000,60000,70000]
#     }
# )

# df3 = pd.merge(df1,df2, on="EmpId",how = "left")
#df3 = pd.merge(df1,df2, on="EmpId",how = "right")
#df3 = pd.merge(df1,df2, on="EmpId",how = "outer")
# df3 = pd.merge(df1,df2, on="EmpId",how = "inner")
# print(df3)

#merging data from csv files
# df1 = pd.read_csv("one.csv")
# df2 = pd.read_csv("two.csv")

# df3 = pd.merge(df1,df2, on="EmpId")
# print(df3)

# df1 = pd.DataFrame({
#     "Name" : ["Emp1","Emp2"]
# })

# df2 = pd.DataFrame({
#     "Name" : ["Emp3","Emp4"]
# })

# df3 = pd.concat([df1,df2])
# print(df3)
# df4 = pd.concat([df1,df2],axis=1)
# print(df4)
