class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n) - time complexity, since each node is visited once
def is_mirror(root1: TreeNode, root2: TreeNode) -> bool:
    if root1 is None and root2 is None:
        return True
    
    if root1 is None or root2 is None:
        return False
    
    return (root1.val == root2.val and
            is_mirror(root1.right, root2.left) and
            is_mirror(root1.left, root2.right))