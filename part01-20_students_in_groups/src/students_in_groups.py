# Write your solution here
students = int(input("How many students on the course? "))
group = int(input("Desired group size? "))

form = students // group
# form1 = form + 1
remain = students % group

if remain == 0:
  print(f"Number of groups formed: {form}")
else:
  print(f"Number of groups formed: {form+1}")
