import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#line plot
#data reading from csv file
# months = ["Jan","Feb","Mar","Apr","May","Jun"]
# sales = [120,150,180,170,210,250]
#df = pd.read_csv('sales.csv')
# df = pd.read_excel('sales.xlsx')
# months = df["Months"]
# sales = df["Sales"]
# plt.figure(figsize=(10,6))
# plt.plot(months,
#                 sales,
#                 color='blue',
#                 linewidth=3,
#                 linestyle='--',

#                 marker='o',
#                 markersize=10,
                
#                 markerfacecolor='yellow',
#                 markeredgecolor='red',
#                 markeredgewidth=2,
#                 label='Months Sales')
# plt.title('Monthly Sales Data', fontsize=16, fontweight='bold')
# plt.xlabel('Months',fontsize=14)
# plt.ylabel('Sales',fontsize=14)
# plt.xlim("Jan","Jun")
# plt.ylim(100,300)
# plt.legend()
# plt.annotate("Highest Sales",
#               xy=('Jun',250),
#               xytext=('Apr',270),
#               arrowprops= dict(facecolor='black',shrink=0.01))
# plt.grid(True)
# plt.savefig("ravi.jpg")
# plt.show()


# subjects = ["Python","Java","React","SQL","AWS"]
# marks = [95,85,70,60,90]
# colors = ['gold','skyblue','lightgreen','orange','pink']
# df = pd.read_excel('subjects_marks.xlsx')
# subjects = df['subjects']  # String data for labels
# marks = df['marks']        # Numeric data for the pie chart

# # Rest of your code remains the same
# colors = df['colors']  # Make sure this column exists in your Excel file
# explode = (0.1,0,0,0,0)
# plt.figure(figsize=(8,8))
# pie_chart = plt.pie(marks,
#                     labels=subjects,
#                     colors=colors,
#                     explode=explode,
#                     autopct='%1.1f%%',
#                     startangle=90,
#                     shadow=True,
#                     counterclock=True,
#                     radius=0.9,
#                     pctdistance=0.7,
#                     labeldistance=1.1,
#                     wedgeprops={
#                         'edgecolor':'black',
#                         'linewidth':2
#                     },
#                     textprops= {
#                         'fontsize' :12,
#                         'color': 'black'
#                     })
# plt.title("Student marks distribution ",fontsize=18,fontweight='bold')
# plt.legend(title="Subjects",loc="upper right")
# plt.savefig("pie-char.jpg")
# plt.show()

#Scatter plot 
# study_hours = [1,2,3,4,5,6,7,8]
# marks = [35,42,50,60,68,75,88,95]
# sizes = [80,100,120,140,160,180,200,220]
# colors = ['red','green','blue','orange','purple','brown','pink','cyan']
# df = pd.read_excel("study_hours_marks.xlsx")
# study_hours = df['study_hours']
# marks = df['marks']
# sizes = df['sizes']
# colors = df['colors']
# plt.figure(figsize=(10,6))
# plt.scatter(study_hours,
#             marks,
#             s=sizes,
#             c=colors,
#             marker='o',
#             alpha=0.8,
#             edgecolors='black',
#             linewidths=2,
#             label="Students"
#             )
# plt.title("Study Hours Vs Marks", fontsize=18,color="red",fontweight="bold")
# plt.xlabel("Study Hours",fontsize=12,color="red")
# plt.ylabel("Marks",fontsize=12,color="red")
# plt.grid(True,linestyle='--',alpha=0.9)
# plt.xlim(0,9)
# plt.ylim(30,100)
# plt.annotate("Top Student",
#              xy=(8,95),
#              xytext=(6.5,90),
#              arrowprops=dict(facecolor='red',shrink=0.05))
# plt.legend()
# plt.savefig("student_marks.jpg")
# plt.show()

#histo plot

# marks = [34,40,42,45,48,
#          50,52,55,59,60,
#          62,65,68,70,72,
#          75,78,80,82,85,
#          88,90,92,95]
# df = pd.read_excel("hist_plot.xlsx")
# marks = df['marks']
# plt.figure(figsize=(10,6))
# plt.hist(marks,
#          bins=6,
#          color='skyblue',
#          edgecolor='black',
#          linewidth=2,
#          alpha=0.8,
#          histtype='stepfilled',
#          rwidth=0.9,
#          label ='Students')
# plt.title("Student Marks Distributed",fontsize=18,fontweight='bold')
# plt.xlabel("Marks",fontsize=12)
# plt.ylabel("Number of Students",fontsize=12)
# plt.grid(axis='x',linestyle='--',alpha=0.5)
# plt.xlim(30,100)
# plt.ylim(0,6)
# plt.legend()
# plt.savefig("histo_plot.jpg")
# plt.show()
# df = pd.DataFrame({
#    "marks" :[34,40,42,45,48,
#          50,52,55,59,60,
#          62,65,68,70,72,
#          75,78,80,82,85,
#          88,90,92,95]
# })

# df.to_excel("hist_plot.xlsx", index=False)

# print("Excel file 'study_data.xlsx' created successfully.")


#sub-plot
# df = pd.read_excel("scatter_plot.xlsx")
# subjects = df['subjects']
# marks = df['marks']
# # subjects = ["Python","Java","React","SQL"]
# # marks = [95,85,75,90]

# plt.figure(figsize=(12,8))
# plt.subplot(2,2,1)
# plt.plot(subjects,marks,marker='o')
# plt.title("Line Plot")

# plt.subplot(2,2,2)
# plt.bar(subjects,marks,color='orange')
# plt.title("Bar Chart")

# plt.subplot(2,2,3)
# plt.pie(marks,labels=subjects,autopct='%f%%')
# plt.title("Pie Chart")

# plt.subplot(2,2,4)
# plt.hist(marks,bins=4,color='green',edgecolor='black')
# plt.title("Histo Plot")
# plt.tight_layout()
# plt.savefig("scatter_plot.jpg")
# plt.show()
# df = pd.DataFrame({
#     'subjects': ["Python", "Java", "React", "SQL"],  # Added quotes around 'subjects'
#     'marks': [95, 85, 75, 90]                       # Added quotes around 'marks'
# })


# df.to_excel("scatter_plot.xlsx", index=False)

# print("Excel file 'study_data.xlsx' created successfully.")


#box plot

# marks = [35,40,45,50,55,
#          60,65,70,75,80,
#          85,90,95,98,150]
# plt.figure(figsize=(8,6))
# plt.boxplot(marks,
#             notch=True,
#             vert=True,
#             patch_artist=True,
#             widths=0.5,
#             showmeans=False,
#             showfliers=False,
#             label=['Students'],
#             boxprops=dict(facecolor='skyblue',color='blue',linewidth=2),
#             medianprops=dict(color='red',linewidth=3),
#             whiskerprops=dict(color='green',linewidth=2),
#             capprops=dict(color='orange',linewidth=2),
#             flierprops=dict(marker='o',markerfacecolor='red',markersize=10)
#             )
# plt.show()


# """
# to display relationship between 2 values 

# example experience and salary relation we use scattor plotter library
# """
#Example-1 (Scatter Plot)
# tips = sns.load_dataset("tips")
# #print(tips.head())
# tips = tips.head()
# sns.scatterplot(x="total_bill",y="tip",data=tips)

# plt.show()

#Example-2 (Histo Plot)
# """
# to know data distribution we use histo plot
#to show the analysis on graph like curve displayed in the output we use kde=True
# """

# tips = sns.load_dataset("tips")
# sns.histplot(tips["total_bill"],bins=20,kde=True)
# plt.show()

#Example-3 (Box Plot)
# """
# to find the least value , highest value, mean value, median value , we use box plot
# """

# tips = sns.load_dataset("tips")
# sns.boxplot(
#     x="day",
#     y="total_bill",
#     data=tips
# )
# plt.show()

#Example-4 (HeatMap)
# """
# to show 25% of data, 50% of data... 
# to show data based on distributions we use HeatMap
# """

# tips = sns.load_dataset("tips")
# corr = tips.corr(numeric_only=True)
# sns.heatmap(
#     corr,
#     annot=True,
#     cmap="coolwarm"
# )
# plt.show()

#Example-5 (pair plot)

# tips = sns.load_dataset("tips")
# sns.pairplot(tips)
# plt.show()



# taxis = sns.load_dataset("taxis")
# print(taxis.head())


# iris = sns.load_dataset("iris")
# print(iris.head())
# pre-defined datasets

# anagrams
# anscombe
# attention
# brain_networks
# car_crashes
# diamonds
# dots
# dowjones
# exercise
# flights
# fmri
# geyser
# glue
# healthexp
# iris
# mpg
# penguins
# planets
# seaice
# taxis
# tips
# titanic
