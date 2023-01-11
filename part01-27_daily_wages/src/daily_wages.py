# Write your solution here

hwage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")

total = hwage * hours

if day == "Sunday":
  total = (hwage*2) * hours

print(f"Daily wages: {total} euros")