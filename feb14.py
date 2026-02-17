# tree implementation using list
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode({self.value})"
# Example usage
if __name__ == "__main__":
    root = TreeNode("root")
    child1 = TreeNode("child1")
    child2 = TreeNode("child2")
    child3 = TreeNode("child3")

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child3)

    print(root)  # Output: TreeNode(root)
    print(root.children)  # Output: [TreeNode(child1), TreeNode(child2)]
    print(child1.children)  # Output: [TreeNode(child3)]

# bst implementation using list
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def __repr__(self):
        return f"BSTNode({self.value})"
# Example usage
if __name__ == "__main__":
    bst = BSTNode(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)

    print(bst)  # Output: BSTNode(10)
    print(bst.left)  # Output: BSTNode(5)
    print(bst.right)  # Output: BSTNode(15)
    print(bst.left.left)  # Output: BSTNode(3)
    print(bst.left.right)  # Output: BSTNode(7)
    