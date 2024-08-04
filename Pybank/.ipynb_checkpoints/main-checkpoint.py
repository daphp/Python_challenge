import os
import pandas as pd
from IPython.display import FileLink

# Load the dataset from the specified directory
df = pd.read_csv('Resources/budget_data.csv')

# Calculate the total number of months included in the dataset
total_months = df.shape[0]

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = df['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
df['Change'] = df['Profit/Losses'].diff()

# Calculate the average of those changes
average_change = df['Change'].mean()

# Find the greatest increase in profits (date and amount) over the entire period
greatest_increase = df.loc[df['Change'].idxmax()]
greatest_increase_date = greatest_increase['Date']
greatest_increase_amount = greatest_increase['Change']

# Find the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = df.loc[df['Change'].idxmin()]
greatest_decrease_date = greatest_decrease['Date']
greatest_decrease_amount = greatest_decrease['Change']

# Prepare the output
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})"
)

# Print the output
print(output)

# Export the results to a text file in the specified directory
output_directory = 'analysis'
output_path = f'{output_directory}/financial_analysis.txt'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

with open(output_path, 'w') as file:
    file.write(output)

# Display a link to download the file
display(FileLink(output_path))
