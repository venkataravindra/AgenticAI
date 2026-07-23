import matplotlib.pyplot as plt
months = ["Jan","Feb","Mar","Apr","May","Jun"]
sales = [100,120,140,180,220,300]

plt.figure(figsize=(10,6))
bars = plt.bar(months,sales,color='skyblue',edgecolor='black',linewidth=2,width=0.6,label='sales')
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 3,
             bar.get_height(),#data to display
             ha = 'center',
             fontsize=10,
             fontweight='bold',
             color='red')
plt.xlabel("Months",fontsize=12)
plt.ylabel("Sales",fontsize=12)
plt.title("Months and Sales Data")
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.xlim(2.5,5.5)
plt.ylim(100,300)
plt.annotate("Highest Sales",
             xy=(5,300),
             xytext=(4,310),
             arrowprops=dict(facecolor='red',shrink=0.05),
             fontsize=11)
plt.savefig("bars.jpg")
plt.show()
