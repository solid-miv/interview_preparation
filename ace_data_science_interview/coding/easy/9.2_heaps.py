"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.
"""
import heapq
from typing import List

# O(n*logn) time complexity
def get_triplet_max_product(arr: List[int]):
    assert len(arr) >= 3, "Array must have at least 3 elements"

    arr = sorted(arr) # O(n*logn) time complexity

    return max(arr[0] * arr[1] * arr[-1], arr[-1] * arr[-2] * arr[-3])

# O(n) time complexity
def get_triplet_max_product_2(arr: List[int]):
    assert len(arr) >= 3, "Array must have at least 3 elements"

    a = heapq.nlargest(3, arr)  # O(n) time complexity
    b = heapq.nsmallest(2, arr)  # O(n) time complexity

    return max(a[0] * a[1] * a[2], a[2] * b[0] * b[1])


if __name__ == "__main__":
    A = [1, 3, 4, 5]
    print(get_triplet_max_product(A))  # 60

    B = [-2, -4, 5, 3]
    print(get_triplet_max_product(B))  # 40