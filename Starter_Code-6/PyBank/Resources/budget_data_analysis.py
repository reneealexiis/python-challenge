import os
import csv

# Path to the CSV file
file_path = os.path.join("budget_data.csv")

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
changes = []
dates = []

# Read the CSV file
with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')

    # Skip the header row
    next(csvreader)

    # Iterate over each row in the CSV file
    for row in csvreader:
        total_months += 1
        profit_loss = int(row[1])
        total_profit_losses += profit_loss

        # Calculate the change in profit/loss
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(row[0])

        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
increase_date = dates[changes.index(greatest_increase)]
decrease_date = dates[changes.index(greatest_decrease)]

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# Export the results to a text file
output_file = "financial_analysis.txt"
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")

print("Results have been saved to 'financial_analysis.txt'")
