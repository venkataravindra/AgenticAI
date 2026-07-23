import matplotlib.pyplot as plt
import pandas as pd

try:
    # Read the Excel file
    df = pd.read_excel('sales.xlsx')
    
    # Check if required columns exist
    if 'months' not in df.columns or 'sales' not in df.columns:
        print("Error: Required columns 'months' and 'sales' not found in the Excel file")
        print(f"Available columns: {df.columns.tolist()}")
    else:
        months = df["months"]
        sales = df["sales"]
        
        plt.figure(figsize=(10,6))
        
        # Plot the data
        plt.plot(months,
                 sales,
                 color='blue',
                 linewidth=3,
                 linestyle='--',
                 marker='o',
                 markersize=10,
                 markerfacecolor='orange',
                 markeredgecolor='red',
                 markeredgewidth=2,
                 label='Months Sales')
        
        # Add title and labels
        plt.title('Monthly Sales Data', fontsize=16, fontweight='bold')
        plt.xlabel('Months', fontsize=14)
        plt.ylabel('Sales', fontsize=14)
        
        # Set axis limits
        plt.ylim(100, 300)
        
        # Add legend
        plt.legend()
        
        # Find the month with highest sales and its value
        max_sales = max(sales)
        max_month = months[sales.idxmax()]
        
        # Annotate the highest sales point
        plt.annotate("Highest Sales",
                     xy=(max_month, max_sales),
                     xytext=(max_month, max_sales + 40),
                     arrowprops=dict(facecolor='black', shrink=0.01),
                     fontsize=12,
                     fontweight='bold',
                     ha='center')
        
        # Add grid
        plt.grid(True)
        
        # Save and show
        plt.savefig("ravi.jpg", dpi=300, bbox_inches='tight')
        plt.show()
        
except FileNotFoundError:
    print("Error: 'sales.xlsx' file not found. Please make sure the file exists in the current directory.")
except Exception as e:
    print(f"An error occurred: {e}")