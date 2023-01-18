# Write your solution here

number = int(input("Please type in a number: "))
 
up = 1
down = number
 
while up < down:
    print(up)
    print(down)
    up += 1
    down -= 1
 
if up == down:
    print(up)