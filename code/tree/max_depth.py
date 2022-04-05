class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root is None:
        return 0

    left_depth = maxDepth(root.left)
    rigth_depth = maxDepth(root.right)
    return max(left_depth, rigth_depth) + 1

tree = TreeNode()
tree.left = TreeNode()
tree.left.left = TreeNode()
tree.left.left.left = TreeNode()
tree.right = TreeNode()

print(maxDepth(tree))