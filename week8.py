#BINARY SEARCH TREE
CODE:
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root
    
    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root
    
    def delete(self, root, key):
        if root is None:
            return root
        
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

tree = BST()

while True:
    print("\n\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter value to insert: "))
        tree.root = tree.insert(tree.root, data)
        print("Node inserted successfully.")

    elif choice == 2:
        key = int(input("Enter value to search: "))
        result = tree.search(tree.root, key)

        if result:
            print("Element found.")
        else:
            print("Element not found.")

    elif choice == 3:
        key = int(input("Enter value to delete: "))
        if tree.search(tree.root, key):
            tree.root = tree.delete(tree.root, key)
            print("Node deleted successfully.")
        else:
            print("Element not found.")

    elif choice == 4:
        print("Inorder Traversal:", end=" ")
        tree.inorder(tree.root)

    elif choice == 5:
        print("Preorder Traversal:", end=" ")
        tree.preorder(tree.root)

    elif choice == 6:
        print("Postorder Traversal:", end=" ")
        tree.postorder(tree.root)

    elif choice == 7:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")
