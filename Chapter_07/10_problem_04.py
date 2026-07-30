"""Take an integer input from the user (e.g., 1432)
 and use a loop to calculate the sum of its individual 
 digits (1 + 4 + 3 + 2 = 10). Do not convert the integer to a string"""

num = int(input("Enter your number: "))
num1 = num
total_sum = 0
while num1 > 0:

    sum_digit = num1%10
    num1 = num1//10
    total_sum = total_sum+sum_digit

print(f"The sum_digit of digits of {num} is = {total_sum}")


