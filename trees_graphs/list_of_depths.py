"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.

listify_depths uses DFS

listify_depths_2 uses BFS
"""
import queue
import copy
import time
from collections import defaultdict

# Linked List Node
class LinkedNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# Binary Tree Node
class BinaryNode:
    def __init__(self, data, left = None, right = None, distance = 0):
        self.data = data
        self.left = left
        self.right = right
        self.distance = distance

# O(n); n is the number of elements in the tree
def listify_depths(root):
    """
    Given a binary tree, function creates a linked list of all the nodes 
    at each depth with a help of DFS.

    Args:
        root (BinaryNode): Root of the binary tree.
    
    Returns:
        list[LinkedNode]: A list of linked lists.
    """
    def next_states(node):
        states = []

        if node.left: states.append(node.left)
        if node.right: states.append(node.right)

        return states

    def listify_dfs(root, next_states):
        count = 0
        table = defaultdict(list)

        root.distance = count
        table[count].append(root)

        to_do = queue.LifoQueue()
        to_do.put(root)

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
    
    table = listify_dfs(root, next_states)

    linked_lists = []

    for key in table:
        first_node = LinkedNode(table[key][0].data)
        linked_lists.append(first_node)
        current = first_node

        for i in range(1, len(table[key])):
            current.next = LinkedNode(table[key][i].data)
            current = current.next

    return linked_lists

# O(n); n is the number of elements in the tree
def listify_depths_2(root):
    """
    Given a binary tree, function creates a linked list of all the nodes 
    at each depth with a help of BFS.

    Args:
        root (BinaryNode): Root of the binary tree.
    
    Returns:
        list[LinkedNode]: A list of linked lists.
    """
    def next_states(node):
        states = []

        if node.left: states.append(node.left)
        if node.right: states.append(node.right)

        return states

    def listify_bfs(root, next_states):
        count = 0
        table = defaultdict(list)

        root.distance = count
        table[count].append(root)

        to_do = queue.Queue()
        to_do.put(root)

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
    
    table = listify_bfs(root, next_states)

    linked_lists = []

    for key in table:
        first_node = LinkedNode(table[key][0].data)
        linked_lists.append(first_node)
        current = first_node

        for i in range(1, len(table[key])):
            current.next = LinkedNode(table[key][i].data)
            current = current.next

    return linked_lists


if __name__ == '__main__':
    # root = BinaryNode(1, 
    #                   BinaryNode(2, 
    #                              BinaryNode(3, 
    #                                         BinaryNode(4, 
    #                                                    BinaryNode(5, 
    #                                                               BinaryNode(6, 
    #                                                                          BinaryNode(7, 
    #                                                                                     BinaryNode(8, 
    #                                                                                                BinaryNode(9, 
    #                                                                                                           BinaryNode(10, 
    #                                                                                                                      BinaryNode(11, 
    #                                                                                                                                 BinaryNode(12, 
    #                                                                                                                                            BinaryNode(13, 
    #                                                                                                                                                       BinaryNode(14, 
    #                                                                                                                                                                  BinaryNode(15, 
    #                                                                                                                                                                             BinaryNode(16))))))))))))))))
    
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4), BinaryNode(5)), BinaryNode(3, BinaryNode(6), BinaryNode(7)))

    # first_start = time.time()
    linked_lists = listify_depths_2(root)
    # first_end = time.time()

    # second_start = time.time()
    # linked_lists_2 = listify_depths_2(root)
    # second_end = time.time()

    # print(f"DFS: {first_end - first_start}")
    # print(f"BFS: {second_end - second_start}")

    for linked_list in linked_lists:
        current = linked_list

        while current:
            print(current.data, end = ' ')
            current = current.next

        print()