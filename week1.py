
# WEEK 1 - LOOPS AND COMMENTS
# This is a single-line comment
"""
This is a
multi-line comment
"""

# Program 1
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)


# Program 2
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)


# Program 3
n = int(input("Enter a number: "))
even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers:", even)
print("Odd numbers:", odd)


# Program 4
a = int(input("Enter a number: "))

for i in range(2, a + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)


# Program 5
a = int(input("Enter no. of rows: "))

for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(i, end="*")
    print()


# Program 6
a = "hello world hello world hello"
s = a.split()
new = {}

for word in s:
    new[word] = new.get(word, 0) + 1

print(new)


# Program 7
a = "greeks for geeks"
b = "everyone can use greeks for geeks"

new1 = a.split()
new2 = b.split()

for word in new2:
    if word not in new1:
        print(word)

print()


# Program 8
list = []

for i in range(1, 101):
    list.append(i)

for m in range(2, 10):
    list.remove(list[m])

n = int(input("Enter a number: "))

if n in list:
    print("Lucky number")
else:
    print("Not a lucky number")
