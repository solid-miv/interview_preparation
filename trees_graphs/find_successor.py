"""
Find a successor: Write an algorithm to find the 'next' node 
(i.e., in-order successor) of a given node in a binary search tree.
You may assume that each node has a link to its parent.
"""
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

# Brute force; O(n); n is the number of elements in the binary tree
def find_successor(root, node_data):
    """
    Given a binary tree and a node, function finds the in-order successor of the node.

    Args:
        root (BinaryNode): Root of the binary tree.
        node_data (int): Data of the node to find the successor of.
    
    Returns:
        int: Data of the in-order successor of the node, -1 if the node specified is the last node in the tree or node was not found.
    """
    tree_iterator = iter(root.in_order_gen())

    root_object = next(tree_iterator)

    while root_object:
        if root_object == node_data:
            return next(tree_iterator, -1)

        root_object = next(tree_iterator, None)

    return -1


if __name__ == "__main__":
    # Generate a binary search tree
    root = BinaryNode(5, 
                      BinaryNode(3, BinaryNode(2), BinaryNode(4)), 
                      BinaryNode(7, BinaryNode(6), BinaryNode(8)))
    
    node_data = 5

    successor = find_successor(root, node_data)

    print(f"Successor of {node_data} is {successor}")