# Program 1

def fun(x):
    x[0] = 20

b = [10, 30, 40, 50, 20]
fun(b)
print(b)

def fun2(x):
    x = 20

a = 10
fun2(a)
print(a)


# Program 2

def B():
    print("inside method A")

def A():
    print("inside method B")
    return B

func = A()
func()


# Program 3

def fun(x):
    if x == 0:
        return 0
    else:
        return 2 * x

b = fun(8)
print(b)


# Program 4

n = input("Enter something: ")

def fun(n):
    if len(n) == 0:
        print("hello")
    else:
        print(n)

fun(n)


# Program 5

a = int(input("Enter a value: "))
b = int(input("Enter a value: "))

def sum(a, b):
    c = a + b
    return c

result = sum(a, b)
print(result)


# Program 6

def fun(n):
    for i in range(1, n + 1):
        print("GFG")

n = int(input("Enter a number: "))
fun(n)


# Program 7

def square(n):
    return n * n

n = int(input("Enter a number: "))
print("Square:", square(n))


# Program 8

def largest(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Largest:", largest(a, b))


# Program 9

def greet(name):
    print("Hello", name)

name = input("Enter your name: ")
greet(name)
