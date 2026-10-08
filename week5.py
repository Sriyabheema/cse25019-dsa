# ============================================================
# WEEK 5
# STACK USING ARRAY AND STACK USING LINKED LIST
# ============================================================


# ============================================================
# 1. STACK USING ARRAY
# ============================================================

stack = []


def push():
    element = int(input("Enter element to push: "))
    stack.append(element)
    print(element, "pushed into stack")


def pop_stack():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack.pop(), "popped from stack")


def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element is:", stack[-1])


def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements are:")

        for i in reversed(stack):
            print(i)


def stack_using_array():
    while True:
        print("\n--- STACK USING ARRAY ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            push()

        elif choice == 2:
            pop_stack()

        elif choice == 3:
            peek()

        elif choice == 4:
            display()

        elif choice == 5:
            print("Program ended")
            break

        else:
            print("Invalid choice")


# ============================================================
# 2. STACK USING LINKED LIST
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self):
        element = int(input("Enter element to push: "))

        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node

        print(element, "pushed into stack")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print(self.top.data, "popped from stack")
            self.top = self.top.next

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element is:", self.top.data)

    # Display operation
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top

            print("Stack elements are:")

            while temp is not None:
                print(temp.data)
                temp = temp.next


def stack_using_linked_list():
    s = LinkedStack()

    while True:
        print("\n--- STACK USING LINKED LIST ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            s.push()

        elif choice == 2:
            s.pop()

        elif choice == 3:
            s.peek()

        elif choice == 4:
            s.display()

        elif choice == 5:
            print("Program ended")
            break

        else:
            print("Invalid choice")


# ============================================================
# MAIN MENU - WEEK 5
# ============================================================

while True:
    print("\n========================================")
    print("             WEEK 5 PROGRAMS")
    print("========================================")
    print("1. Stack Using Array")
    print("2. Stack Using Linked List")
    print("3. Exit")
    print("========================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        stack_using_array()

    elif choice == 2:
        stack_using_linked_list()

    elif choice == 3:
        print("Week 5 program ended")
        break

    else:
        print("Invalid choice")
