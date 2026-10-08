# ============================================================
# WEEK 6
# QUEUE USING ARRAY, LINKED LIST AND CIRCULAR LINKED LIST
# ============================================================


# ============================================================
# 1. QUEUE USING ARRAY
# ============================================================

class QueueArray:

    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, x):

        if self.rear == self.size - 1:
            print("Queue Overflow")

        else:

            if self.front == -1:
                self.front = 0

            self.rear += 1
            self.queue[self.rear] = x

            print(f"{x} inserted into the queue")

    def dequeue(self):

        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")

        else:

            x = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1

            print(f"{x} deleted from the queue")

            if self.front > self.rear:
                self.front = -1
                self.rear = -1

    def peek(self):

        if self.front == -1:
            print("Queue is empty")

        else:
            print("Front element:", self.queue[self.front])

    def display(self):

        if self.front == -1:
            print("Queue is empty")

        else:

            print("The elements of the queue are:")

            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


def queue_using_array():

    size = int(input("Enter the size of Queue: "))
    q = QueueArray(size)

    while True:

        print("\n----- QUEUE USING ARRAY -----")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            item = int(input("Enter the element to enqueue: "))
            q.enqueue(item)

        elif choice == 2:
            q.dequeue()

        elif choice == 3:
            q.peek()

        elif choice == 4:
            q.display()

        elif choice == 5:
            print("Exiting Queue Using Array")
            break

        else:
            print("Invalid choice")


# ============================================================
# 2. QUEUE USING LINKED LIST
# ============================================================

class QueueLinkedList:

    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, x):

        if self.rear == self.size - 1:
            print("Queue Overflow")

        else:

            if self.front == -1:
                self.front = 0

            self.rear += 1
            self.queue[self.rear] = x

            print(f"{x} inserted into the queue")

    def dequeue(self):

        if self.front == -1:
            print("Queue Underflow")

        else:

            x = self.queue[self.front]
            self.queue[self.front] = None

            print(f"{x} deleted from the queue")

            self.front += 1

            if self.front > self.rear:
                self.front = -1
                self.rear = -1

    def peek(self):

        if self.front == -1:
            print("Queue is empty")

        else:
            print("Front element:", self.queue[self.front])

    def display(self):

        if self.front == -1:
            print("Queue is empty")

        else:

            print("The elements of the queue are:")

            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


def queue_using_linked_list():

    size = int(input("Enter the size of Queue: "))
    q = QueueLinkedList(size)

    while True:

        print("\n----- QUEUE USING LINKED LIST -----")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            item = int(input("Enter the element to enqueue: "))
            q.enqueue(item)

        elif choice == 2:
            q.dequeue()

        elif choice == 3:
            q.peek()

        elif choice == 4:
            q.display()

        elif choice == 5:
            print("Exiting Queue Using Linked List")
            break

        else:
            print("Invalid Choice!")


# ============================================================
# 3. QUEUE USING CIRCULAR LINKED LIST
# ============================================================

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:

    def __init__(self, size=5):
        self.size = size
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, x):

        if self.count == self.size:
            print("Queue Overflow")

        else:

            new_node = Node(x)

            if self.front is None:

                self.front = new_node
                self.rear = new_node
                new_node.next = new_node

            else:

                new_node.next = self.front
                self.rear.next = new_node
                self.rear = new_node

            self.count += 1

            print(f"{x} inserted into the queue")

    def dequeue(self):

        if self.front is None:
            print("Queue Underflow")

        else:

            x = self.front.data

            if self.front == self.rear:

                self.front = None
                self.rear = None

            else:

                self.front = self.front.next
                self.rear.next = self.front

            self.count -= 1

            print(f"{x} deleted from the queue")

    def peek(self):

        if self.front is None:
            print("Queue is empty")

        else:
            print("Front element:", self.front.data)

    def display(self):

        if self.front is None:
            print("Queue is empty")

        else:

            print("The elements of the queue are:")

            temp = self.front

            while True:

                print(temp.data)
                temp = temp.next

                if temp == self.front:
                    break


def queue_using_circular_linked_list():

    size = int(input("Enter the size of Queue: "))
    q = CircularQueue(size)

    while True:

        print("\n----- CIRCULAR LINKED LIST QUEUE -----")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            item = int(input("Enter the element to enqueue: "))
            q.enqueue(item)

        elif choice == 2:
            q.dequeue()

        elif choice == 3:
            q.peek()

        elif choice == 4:
            q.display()

        elif choice == 5:
            print("Exiting Circular Linked List Queue")
            break

        else:
            print("Invalid Choice!")


# ============================================================
# MAIN MENU - WEEK 6
# ============================================================

while True:

    print("\n========================================")
    print("             WEEK 6 PROGRAMS")
    print("========================================")
    print("1. Queue Using Array")
    print("2. Queue Using Linked List")
    print("3. Queue Using Circular Linked List")
    print("4. Exit")
    print("========================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        queue_using_array()

    elif choice == 2:
        queue_using_linked_list()

    elif choice == 3:
        queue_using_circular_linked_list()

    elif choice == 4:
        print("Week 6 program ended")
        break

    else:
        print("Invalid choice")
