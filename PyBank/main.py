import os
import csv

# Getting the folder's path
file_path = os.path.join(".", "Resources", "budget_data.csv")

# Define the Function
def financial_analysis(file_path):
    # initialize variables
    months = []
    profit_loss = []
    change = []

    # Read data into lists
    with open(file_path, "r") as budget_data:
        budget_data = csv.reader(budget_data, delimiter=",")
        header = next(budget_data)
        for row in budget_data:
            months.append(row[0])
            profit_loss.append(int(row[1]))

    # Calculate the total number of months included in the dataset
    total_months = len(months)
    # The net total amount of "Profit/Losses" over the entire period
    total_profit_loss = sum(profit_loss)

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for i in range(1, len(profit_loss)):
        change.append(profit_loss[i] - profit_loss[i - 1])

    if change:
        avg_change = round(sum(change) / len(change), 2)
    else:
        avg_change = 0

    # Find the greatest increase in profits (date and amount) over the entire period
    if change:
        greatest_increase = max(change)
        greatest_increase_month = months[change.index(greatest_increase) + 1]
    else:
        greatest_increase = 0
        greatest_increase_month = ''

    # Find the greatest decrease in profits (date and amount) over the entire period
    if change:
        greatest_decrease = min(change)
        greatest_decrease_month = months[change.index(greatest_decrease) + 1]
    else:
        greatest_decrease = 0
        greatest_decrease_month = ''

    # print the results
    print(f"Financial Analysis")
    print(f"-----------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

    # Save the results into financial_analysis.txt
    output_file = os.path.join(".", "analysis", "financial_analysis_results.txt")
    with open(output_file, "w", newline="") as file:
        file.write("Financial Analysis\n")
        file.write("-----------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${total_profit_loss}\n")
        file.write(f"Average Change: ${avg_change}\n")
        file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
        file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")


# Call the function
financial_analysis(file_path)
