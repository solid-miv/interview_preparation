# Binary tree node class
class BinaryNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# O(n); n is the number of elements in the array
def min_tree(arr):
    """
    Given a sorted (increasing order) array with unique integer elements, 
    function creates a binary search tree with minimal height.

    Args:
        arr (list[int]): Sorted array with unique integer elements.
    
    Returns:
        BinaryNode: Root of the binary search tree.
    """
    def min_tree_supp(arr, start, end):
        if start > end:
            return BinaryNode(None)

        if start == end:
            return BinaryNode(arr[start])

        mid = (start + end) // 2

        root = BinaryNode(arr[mid])
        root.left = min_tree_supp(arr, start, mid-1)  # using slicing arr[:mid] makes dividing the array O(n) -> this division is O(1)
        root.right = min_tree_supp(arr, mid+1, end)

        return root
    
    return min_tree_supp(arr, 0, len(arr)-1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    answ = min_tree(arr)

    print(answ.data)
    print(answ.left.data)
    print(answ.right.data)

    print(answ.left.left.data)
    print(answ.left.right.data)

    print(answ.right.left.data)
    print(answ.right.right.data)