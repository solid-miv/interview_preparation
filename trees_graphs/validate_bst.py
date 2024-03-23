class BinaryNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def in_order_gen(self):
        """
        In-order traversal means to 'visit' the left branch, then the current node, and finally, the right branch.
        When performed on a binary search tree, it visits the nodes in ascending order (hence the name 'in-order').
        """
        if self.left:
            yield from self.left.in_order_gen()  # same as 'for value in self.left.in_order_gen(): yield value'
        
        yield self.data

        if self.right:
            yield from self.right.in_order_gen()

# O(n); n is the number of elements in the binary tree
def validate_bst(root):
    """
    Given a binary tree, function checks if the tree is a binary search tree.

    Args:
        root (BinaryNode): Root of the binary tree.

    Returns:
        bool: True if the tree is a binary search tree, False otherwise.
    """
    node_iter = iter(root.in_order_gen())

    current_node_data = next(node_iter)
    next_node_data = next(node_iter)

    while next_node_data:
        if current_node_data > next_node_data:
            return False

        current_node_data = next_node_data
        next_node_data = next(node_iter, None)  # None is a default value to be returned if there are no more items to return
    
    return True


if __name__ == '__main__':
    root = BinaryNode(1, left=None, right=BinaryNode(3, left=BinaryNode(4)))

    answ = validate_bst(root)

    print(answ)