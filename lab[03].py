class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    # Traversals
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    # Search with path
    def search(self, root, key):
        path = []
        current = root
        while current:
            path.append(current.key)
            if key == current.key:
                print(f"Key {key} found ✅ Path: {path}")
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        print(f"Key {key} not found ❌ Path taken: {path}")
        return False

    # Find min (helper for delete)
    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    # Delete a node
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Case 1: Leaf node
            if root.left is None and root.right is None:
                return None
            # Case 2: One child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Case 3: Two children
            else:
                min_node = self.find_min(root.right)
                root.key = min_node.key
                root.right = self.delete(root.right, min_node.key)

        return root

    # Height of tree
    def height(self, root):
        if root is None:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    # Check if balanced
    def is_balanced(self, root):
        if root is None:
            return True

        left_h = self.height(root.left)
        right_h = self.height(root.right)

        if abs(left_h - right_h) > 1:
            return False

        return self.is_balanced(root.left) and self.is_balanced(root.right)


# -------- Main Program ----------
bst = BST()
numbers = [50, 30, 20, 40, 70, 60, 80]   # Example input

for num in numbers:
    bst.insert_key(num)

print("Inorder Traversal: ", end="")
bst.inorder(bst.root)

print("\nPreorder Traversal: ", end="")
bst.preorder(bst.root)

print("\nPostorder Traversal: ", end="")
bst.postorder(bst.root)

print("\n")

# Searching
bst.search(bst.root, 60)   # Present
bst.search(bst.root, 25)   # Not present

# Deletion
print("\nDeleting 30 (one child case)...")
bst.root = bst.delete(bst.root, 30)
print("Inorder after deletion: ", end="")
bst.inorder(bst.root)

print("\nDeleting 20 (leaf case)...")
bst.root = bst.delete(bst.root, 20)
print("Inorder after deletion: ", end="")
bst.inorder(bst.root)

print("\nDeleting 50 (two children case)...")
bst.root = bst.delete(bst.root, 50)
print("Inorder after deletion: ", end="")
bst.inorder(bst.root)

# Height & Balance
h = bst.height(bst.root)
print(f"\n\nHeight of BST: {h}")
if bst.is_balanced(bst.root):
    print("The BST is Balanced ✅")
else:
    print("The BST is Skewed ❌")
