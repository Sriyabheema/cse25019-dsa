# ============================================================
# WEEK 4 - LINKED LISTS AND STACK
# ============================================================


# ============================================================
# 1. SINGLY LINKED LIST
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create / Insert at Beginning
    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
        print("Node inserted at beginning.")

    # Insert at End
    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

        print("Node inserted at end.")

    # Insert at Specific Index
    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.insert_begin(data)
            return

        if self.head is None:
            print("Invalid index.")
            return

        temp = self.head

        for _ in range(index - 1):
            if temp is None:
                print("Invalid index.")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index.")
            return

        new = Node(data)
        new.next = temp.next
        temp.next = new

        print("Node inserted at index", index)

    # Delete by Value
    def delete(self, value):
        if self.head is None:
            print("No data to delete.")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("Value deleted.")
            return

        temp = self.head

        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not present.")
        else:
            temp.next = temp.next.next
            print("Value deleted.")

    # Delete First Node
    def deleteAtBeg(self):
        if self.head is None:
            print("No data to delete.")
        else:
            temp = self.head
            self.head = self.head.next
            print("Deleted Value =", temp.data)

    # Delete Last Node
    def deleteAtEnd(self):
        if self.head is None:
            print("No data to delete.")

        elif self.head.next is None:
            print("Deleted Value =", self.head.data)
            self.head = None

        else:
            temp = self.head

            while temp.next.next:
                temp = temp.next

            print("Deleted Value =", temp.next.data)
            temp.next = None

    # Count Nodes
    def count(self):
        c = 0
        temp = self.head

        while temp:
            c += 1
            temp = temp.next

        print("Number of nodes =", c)

    # Display
    def display(self):
        if self.head is None:
            print("No Linked List")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Singly Linked List Menu
def singly_linked_list():
    ll = LinkedList()

    while True:
        print("\n--- SINGLY LINKED LIST ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Specific Index")
        print("4. Delete by Value")
        print("5. Delete First Node")
        print("6. Delete Last Node")
        print("7. Count Nodes")
        print("8. Display")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            ll.insert_begin(data)

        elif choice == 2:
            data = int(input("Enter data: "))
            ll.insert_end(data)

        elif choice == 3:
            data = int(input("Enter data: "))
            index = int(input("Enter index: "))
            ll.insert_at_index(data, index)

        elif choice == 4:
            value = int(input("Enter value to delete: "))
            ll.delete(value)

        elif choice == 5:
            ll.deleteAtBeg()

        elif choice == 6:
            ll.deleteAtEnd()

        elif choice == 7:
            ll.count()

        elif choice == 8:
            ll.display()

        elif choice == 9:
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


# ============================================================
# 2. DOUBLY LINKED LIST
# ============================================================

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_begin(self, data):
        new_node = DNode(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        print("Node inserted at beginning.")

    # Insert at End
    def insert_end(self, data):
        new_node = DNode(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

        print("Node inserted at end.")

    # Insert at Specific Position
    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_begin(data)
            return

        temp = self.head
        count = 1

        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position.")
            return

        new_node = DNode(data)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print("Node inserted at position", position)

    # Delete by Value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        while temp is not None and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found.")
            return

        if temp.prev is not None:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next is not None:
            temp.next.prev = temp.prev

        print("Value deleted.")

    # Delete Beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty.")
            return

        print("Deleted Value =", self.head.data)

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    # Delete End
    def delete_end(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        if temp.next is None:
            print("Deleted Value =", temp.data)
            self.head = None
            return

        while temp.next is not None:
            temp = temp.next

        print("Deleted Value =", temp.data)
        temp.prev.next = None

    # Count Nodes
    def count(self):
        temp = self.head
        count = 0

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # Display
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("Doubly Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Doubly Linked List Menu
def doubly_linked_list():
    dll = DoublyLinkedList()

    while True:
        print("\n--- DOUBLY LINKED LIST ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Specific Position")
        print("4. Delete by Value")
        print("5. Delete Beginning")
        print("6. Delete End")
        print("7. Count")
        print("8. Display")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            dll.insert_begin(data)

        elif choice == 2:
            data = int(input("Enter data: "))
            dll.insert_end(data)

        elif choice == 3:
            data = int(input("Enter data: "))
            position = int(input("Enter position: "))
            dll.insert_at_position(data, position)

        elif choice == 4:
            value = int(input("Enter value to delete: "))
            dll.delete_by_value(value)

        elif choice == 5:
            dll.delete_begin()

        elif choice == 6:
            dll.delete_end()

        elif choice == 7:
            dll.count()

        elif choice == 8:
            dll.display()

        elif choice == 9:
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


# ============================================================
# 3. CIRCULAR LINKED LIST
# ============================================================

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_begin(self, data):
        new_node = CNode(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

        print("Node inserted at beginning.")

    # Insert at End
    def insert_end(self, data):
        new_node = CNode(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

        print("Node inserted at end.")

    # Insert at Specific Position
    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_begin(data)
            return

        if self.head is None:
            print("Invalid position.")
            return

        new_node = CNode(data)
        temp = self.head
        count = 1

        while temp.next != self.head and count < position - 1:
            temp = temp.next
            count += 1

        if count != position - 1:
            print("Invalid position.")
            return

        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted at position", position)

    # Delete by Value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return

        # Only one node
        if self.head.next == self.head:
            if self.head.data == value:
                self.head = None
                print("Value deleted.")
            else:
                print("Value not found.")
            return

        # Delete head
        if self.head.data == value:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            self.head = self.head.next
            temp.next = self.head

            print("Value deleted.")
            return

        temp = self.head

        while temp.next != self.head and temp.next.data != value:
            temp = temp.next

        if temp.next == self.head:
            print("Value not found.")
        else:
            temp.next = temp.next.next
            print("Value deleted.")

    # Delete Beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next == self.head:
            print("Deleted Value =", self.head.data)
            self.head = None
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        print("Deleted Value =", self.head.data)

        self.head = self.head.next
        temp.next = self.head

    # Delete End
    def delete_end(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next == self.head:
            print("Deleted Value =", self.head.data)
            self.head = None
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        print("Deleted Value =", temp.next.data)

        temp.next = self.head

    # Count Nodes
    def count(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        temp = self.head
        count = 0

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    # Display
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("Circular Linked List:", end=" ")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("HEAD")


# Circular Linked List Menu
def circular_linked_list():
    cll = CircularLinkedList()

    while True:
        print("\n--- CIRCULAR LINKED LIST ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Specific Position")
        print("4. Delete by Value")
        print("5. Delete Beginning")
        print("6. Delete End")
        print("7. Count")
        print("8. Display")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            cll.insert_begin(data)

        elif choice == 2:
            data = int(input("Enter data: "))
            cll.insert_end(data)

        elif choice == 3:
            data = int(input("Enter data: "))
            position = int(input("Enter position: "))
            cll.insert_at_position(data, position)

        elif choice == 4:
            value = int(input("Enter value to delete: "))
            cll.delete_by_value(value)

        elif choice == 5:
            cll.delete_begin()

        elif choice == 6:
            cll.delete_end()

        elif choice == 7:
            cll.count()

        elif choice == 8:
            cll.display()

        elif choice == 9:
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


# ============================================================
# 4. STACK USING ARRAY
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


def peek_stack():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element is:", stack[-1])


def display_stack():
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
            peek_stack()

        elif choice == 4:
            display_stack()

        elif choice == 5:
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


# ============================================================
# 5. STACK USING LINKED LIST
# ============================================================

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    # Push
    def push(self, element):
        new_node = StackNode(element)
        new_node.next = self.top
        self.top = new_node

        print(element, "pushed into stack")

    # Pop
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print(self.top.data, "popped from stack")
            self.top = self.top.next

    # Peek
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element is:", self.top.data)

    # Display
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top

            print("Stack elements are:")

            while temp is not None:
                print(temp.data)
                temp = temp.next


# Stack Using Linked List Menu
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
            element = int(input("Enter element to push: "))
            s.push(element)

        elif choice == 2:
            s.pop()

        elif choice == 3:
            s.peek()

        elif choice == 4:
            s.display()

        elif choice == 5:
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


# ============================================================
# MAIN MENU
# ============================================================

while True:
    print("\n========================================")
    print("             WEEK 4 PROGRAMS")
    print("========================================")
    print("1. Singly Linked List")
    print("2. Doubly Linked List")
    print("3. Circular Linked List")
    print("4. Stack Using Array")
    print("5. Stack Using Linked List")
    print("6. Exit")
    print("========================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        singly_linked_list()

    elif choice == 2:
        doubly_linked_list()

    elif choice == 3:
        circular_linked_list()

    elif choice == 4:
        stack_using_array()

    elif choice == 5:
        stack_using_linked_list()

    elif choice == 6:
        print("Week 4 program ended.")
        break

    else:
        print("Invalid choice.")
