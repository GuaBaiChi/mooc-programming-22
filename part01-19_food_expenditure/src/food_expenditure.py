# Write your solution here
xweek = float(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

totalcafe = xweek * price
weekly = totalcafe + groceries
dailyavg = weekly/7

print("Average food expenditure:")
print(f"Daily: {dailyavg} euros")
print(f"Weekly: {weekly} euros")
