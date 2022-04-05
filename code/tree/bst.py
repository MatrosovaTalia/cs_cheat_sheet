class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def in_order_print(self):
        return self.in_order(self.root, "")

    def in_order(self, node, traversal):
        if node:
            if node.root.left:
                traversal = self.in_order(node.root.left, traversal)
            traversal += (str(node.value) + " - ")
            if node.root.right:
                traversal = self.in_order(node.root.left, traversal)

        return traversal

    def pre_order(self, node):
        if node:

            traversal += str(node.value) + " - "
            traversal = self.in_order(node.left)
            traversal = self.in_order(node.right)

        return traversal

    def post_order(self, node):
        if node:
            traversal = self.in_order(node.left)
            traversal = self.in_order(node.right)
            traversal += str(node.value) + " - "

        return traversal

tree = BinTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree2 = BinTree("F")
tree2.root.left = BinTree("B")
tree2.root.left.left = BinTree("A")
tree2.root.left.right = BinTree("D")
tree2.root.left.right.left = BinTree("C")
tree2.root.left.right.right = BinTree("E")
tree2.root.right = BinTree("G")
tree2.root.right.right = BinTree("I")
tree2.root.right.right.left = BinTree("H")

print(tree2.in_order_print())

