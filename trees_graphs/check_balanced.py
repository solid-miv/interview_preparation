"""
Check Balanced: Implement a function to check if a binary tree is balanced. 
For the purposes of this question, a balanced tree is defined to be a tree
such that the heights of the two subtrees of any node never differ by more than one.

check_balanced calls listify_dfs, which uses DFS
"""
from collections import defaultdict
import queue


class BinaryNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.distance = 0

# O(n); n is the number of elements in the binary tree
def check_balanced(root):
    """
    Given a binary tree, function checks if the tree is balanced.

    Args:
        root (BinaryNode): Root of the binary tree.
    
    Returns:
        bool: True if the tree is balanced, False otherwise.
    """
    def next_states(node):
        neighbours = []

        if node.left: neighbours.append(node.left)
        if node.right: neighbours.append(node.right)

        return neighbours
    
    def listify_dfs(node, next_states):
        count = 0
        table = defaultdict(list)

        node.distance = count
        table[count].append(node)

        to_do = queue.LifoQueue()
        to_do.put(node)

        explored = set()

        while not to_do.empty():
            current = to_do.get()
            count = current.distance + 1

            for state in next_states(current):
                if state not in explored:
                    state.distance = count
                    table[count].append(state)
                    explored.add(state)
                    to_do.put(state)

        return table
    
    table_left = defaultdict(list)
    table_right = defaultdict(list)

    if root.left:
        table_left = listify_dfs(root.left, next_states)
    
    if root.right:
        table_right = listify_dfs(root.right, next_states)

    return abs(len(table_left.keys()) - len(table_right.keys())) <= 1


if __name__ == '__main__':
    # root = BinaryNode(1, 
    #                   BinaryNode(2, 
    #                              BinaryNode(3, 
    #                                         BinaryNode(4, 
    #                                                    BinaryNode(5, 
    #                                                               BinaryNode(6, 
    #                                                                          BinaryNode(7))))), 
    #                              BinaryNode(8, 
    #                                         BinaryNode(9, 
    #                                                    BinaryNode(10, 
    #                                                               BinaryNode(11, 
    #                                                                          BinaryNode(12)))))))

    # root = BinaryNode(1, BinaryNode(2, BinaryNode(4), BinaryNode(5)), BinaryNode(3, BinaryNode(6), BinaryNode(7)))

    root = BinaryNode(1, left=None, right=BinaryNode(3, BinaryNode(4)))

    print(check_balanced(root))