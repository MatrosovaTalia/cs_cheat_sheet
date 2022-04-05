from bst import BinTree



root = BinTree("F")
root.left = BinTree("B")
root.left.left = BinTree("A")
root.left.right = BinTree("D")
root.left.right.left = BinTree("C")
root.left.right.right = BinTree("E")
root.right = BinTree("G")
root.right.right = BinTree("I")
root.right.right.left = BinTree("H")

print(root.in_order_print())
# print("Pre-order: " + pre_order(root))
# print("Post-order: " + post_order(root))
