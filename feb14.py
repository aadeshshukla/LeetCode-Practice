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

