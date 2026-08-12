# Program 1

# Find the first digit of a number using recursion
def first_digit(n):
    if n == 0:
        return 0
    elif n >= 10:
        return first_digit(n // 10)
    else:
        return n

n = int(input("Enter a number: "))
result = first_digit(n)
print("First digit:", result)


# Program 2

# Calculate power using recursion
def intrest(p, n):
    if n == 0:
        return 1
    else:
        return p * intrest(p, n - 1)

n = int(input("Enter no. of years: "))
p = int(input("Enter a number: "))
result = intrest(p, n)
print(result)


# Program 3

# Fibonacci series using recursion
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Enter no. of terms: "))

if n < 0:
    print("Invalid input")
else:
    for i in range(n):
        print(fib(i), end=" ")


# Program 4

# Sum of digits using recursion
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

n = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(n))


# Program 5

# Reverse a number using recursion
def reverse(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse(n // 10, rev * 10 + n % 10)

n = int(input("Enter a number: "))
print("Reverse:", reverse(n))
