#Sum of numbers till num enetered by user

num = int(input("Enter your number: "))

sum = 0
i = 1
while i<=num :
    sum = sum + i
    i+=1
print(f"The sum of numbers fro 1 to {num} is = {sum}")