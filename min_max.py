class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def min_max(node, depth, is_maximizing):
    if depth == 0 or not node.children:
        return node.value

    if is_maximizing:
        best_value = float('-inf')
        for child in node.children:
            value = min_max(child, depth - 1, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for child in node.children:
            value = min_max(child, depth - 1, True)
            best_value = min(best_value, value)
        return best_value


root = TreeNode(3)
root.children.append(TreeNode(5))
root.children.append(TreeNode(2))
root.children[0].children.append(TreeNode(9))
root.children[0].children.append(TreeNode(12))
root.children[1].children.append(TreeNode(6))
root.children[1].children.append(TreeNode(8))

depth = 3  
best_value = min_max(root, depth, True)
print(f"Best value at depth {depth}: {best_value}")