# Program 1

def bubble_sort():
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

n = int(input("Enter no. of elements: "))
arr = []

for i in range(n):
    a = int(input("Enter a number: "))
    arr.append(a)

print("Original list:", arr)

result = bubble_sort()
print("New sorted list:", result)


# Program 2

def insertion_sort():
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

n = int(input("Enter no. of elements: "))
arr = []

for i in range(n):
    a = int(input("Enter a number: "))
    arr.append(a)

print("Original list:", arr)

result = insertion_sort()
print("New sorted list:", result)


# Program 3

def selection_sort():
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

n = int(input("Enter no. of elements: "))
arr = []

for i in range(n):
    a = int(input("Enter a number: "))
    arr.append(a)

print("Original list:", arr)

result = selection_sort()
print("New sorted list:", result)


# Program 4

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = len(arr) // 2
    left = []
    middle = []
    right = []

    for i in range(len(arr)):
        if arr[i] < arr[pivot]:
            left.append(arr[i])
        elif arr[i] == arr[pivot]:
            middle.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + middle + quick_sort(right)

n = int(input("Enter no. of elements: "))
arr = []

for i in range(n):
    a = int(input("Enter a number: "))
    arr.append(a)

print("Original list:", arr)

result = quick_sort(arr)
print("New sorted list:", result)
