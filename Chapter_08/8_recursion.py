
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter the number to find its factorial: "))
fact = factorial(num)
print(f"The factorial of {num} is = {fact}")