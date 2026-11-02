#10.A-Separate Chaining
size = 10
table = [[] for i in range(size)]

def insert(key):
    index = key % size
    table[index].append(key)

def display():
    for i in range(size):
        print(i, ":", table[i])

n = int(input("Enter number of elements: "))
for i in range(n):
    key = int(input("Enter key: "))
    insert(key)

display()

#10.B-Linear Probing
size = 10
table = [-1] * size

def insert(key):
    index = key % size

    while table[index] != -1:
        index = (index + 1) % size

    table[index] = key

def display():
    for i in range(size):
        print(i, ":", table[i])

n = int(input("Enter number of elements: "))
for i in range(n):
    key = int(input("Enter key: "))
    insert(key)

display()

#10.C-Quadratic Probing
size = 10
table = [-1] * size

def insert(key):
    index = key % size
    i = 0

    while i < size:
        new_index = (index + i * i) % size

        if table[new_index] == -1:
            table[new_index] = key
            return

        i += 1

    print("Hash table is full or no slot found")

def display():
    for i in range(size):
        print(i, ":", table[i])

n = int(input("Enter number of elements: "))
for i in range(n):
    key = int(input("Enter key: "))
    insert(key)

display()
