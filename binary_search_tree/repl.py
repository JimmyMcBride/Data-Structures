from binary_search_tree import BinarySearchTreeNode

bst = BinarySearchTreeNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
# print("BST Val:", bst.left.right.value, "Expected Val:", 3)
# print("BST Val:", bst.right.left.value, "Expected Val:", 6)

# bst.for_each(lambda x: print(x))
# bst.in_order_print(bst)
# bst.bft_print(bst)
bst.dft_print(bst)
