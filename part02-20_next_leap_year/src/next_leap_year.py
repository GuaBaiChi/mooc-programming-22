# Write your solution here

def leapyear(year): 
  return(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 ==0));

year = int(input("Year: "))
nextleap = year + 1

while True:
  if leapyear(nextleap) == True:
    print(f"The next leap year after {year} is {nextleap}")
    break
  else:
    nextleap = nextleap + 1






# I used old code from the leap year assignment
# def leapyear(year): 
#   return(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 ==0));

# year = int(input("Year: "))

# if (leapyear(year)):
#   print("That year is a leap year.") 
# else: 
#   print("That year is not a leap year.")



# suggested solution is
# start_year = int(input("Year: "))
# year = start_year + 1

# while True:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             break
#     elif year % 4 == 0:
#         break
#     year += 1

# print(f"The next leap year after {start_year} is {year}")