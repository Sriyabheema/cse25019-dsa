#Binary tree using an array
#code:
class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, value):
        for i in range(self.size):
            if self.tree[i] is None:
                self.tree[i] = value
                print(value, "inserted")
                return
        print("Tree is full")

    def search(self, value):
        for i in range(self.size):
            if self.tree[i] == value:
                print(value, "found at index", i)
                return
        print(value, "not found")

    def delete(self, value):
        for i in range(self.size):
            if self.tree[i] == value:
                self.tree[i] = None
                print(value, "deleted")
                return
        print(value, "not found")

    def inorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    def preorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def postorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")


bt = BinaryTree(10)

while True:
    print("\n1.Insert  2.Delete  3.Search")
    print("4.Inorder  5.Preorder  6.Postorder  7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        bt.insert(value)
    elif choice == 2:
        value = int(input("Enter value to delete: "))
        bt.delete(value)
    elif choice == 3:
        value = int(input("Enter value to search: "))
        bt.search(value)
    elif choice == 4:
        bt.inorder()
        print()
    elif choice == 5:
        bt.preorder()
        print()
    elif choice == 6:
        bt.postorder()
        print()
    elif choice == 7:
        break
    else:
        print("Invalid choice")

  #Binary tree using linked list
  #code:
  class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            print(data, "inserted")
            return
        queue = [self.root]
        
        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                print(data, "inserted")
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                print(data, "inserted")
                return
            else:
                queue.append(current.right)

    def search(self, data):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.data == data:
                print(data, "found")
                return

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        print(data, "not found")

    def delete(self, data):
        if self.root is None:
            print("Tree is empty")
            return
        queue = [self.root]
        target = None
        deepest = None
        parent = None
        deepest_parent = None

        while queue:
            current = queue.pop(0)

            if current.data == data:
                target = current

            if current.left:
                parent = current
                queue.append(current.left)
                deepest_parent = current

            if current.right:
                parent = current
                queue.append(current.right)
                deepest_parent = current

            deepest = current

        if target is None:
            print(data, "not found")
            return

        if deepest == self.root:
            self.root = None
        else:
            if deepest_parent.left == deepest:
                deepest_parent.left = None
            else:
                deepest_parent.right = None
            target.data = deepest.data
        print(data, "deleted")

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

bt = BinaryTree()
while True:
    print("\n1.Insert  2.Delete  3.Search")
    print("4.Inorder  5.Preorder  6.Postorder  7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        bt.insert(value)

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        bt.delete(value)

    elif choice == 3:
        value = int(input("Enter value to search: "))
        bt.search(value)

    elif choice == 4:
        bt.inorder(bt.root)
        print()

    elif choice == 5:
        bt.preorder(bt.root)
        print()

    elif choice == 6:
        bt.postorder(bt.root)
        print()

    elif choice == 7:
        break

    else:
        print("Invalid choice")


  
