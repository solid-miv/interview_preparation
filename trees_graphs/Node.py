class Node:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    # uses generator delegation 
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
    
    # uses generator delegation
    def pre_order_gen(self):
        """
        Pre-order traversal visits the current node before its child nodes (hence the name 'pre-order').
        In a pre-order traversal, the root is always the first node visited.
        """
        yield self.data

        if self.left:
            yield from self.left.pre_order_gen()
        
        if self.right:
            yield from self.right.pre_order_gen()
    
    # uses generator delegation
    def post_order_gen(self):
        """
        Post-order traversal visits the current node after its child nodes (hence the name 'post-order').
        In a post-order traversal, the root is always the last node visited.
        """
        if self.left:
            yield from self.left.post_order_gen()
        
        if self.right:
            yield from self.right.post_order_gen()
        
        yield self.data