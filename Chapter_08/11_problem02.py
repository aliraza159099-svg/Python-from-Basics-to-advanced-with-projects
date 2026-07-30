'''
Wtite a recursive function to print the sum of first n numbers

'''

def sum_of_num(n):
    if n == 1:
        return 1
    return n + sum_of_num(n - 1)

num = int(input("Enter the number : "))
sum = sum_of_num(num)
print(f"The sum of number from 1 to {num} is = {sum}")