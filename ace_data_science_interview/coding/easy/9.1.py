"""
Given two arrays, write a function to compute their intersection.
"""
from typing import List

# O(n + m) time complexity
def get_intersection(arr1: List[int], arr2: List[int]):
    set_arr1 = set(arr1)
    set_arr2 = set(arr2)

    if len(set_arr1) < len(set_arr2):
        return [x for x in set_arr1 if x in set_arr2]
    else:
        return [x for x in set_arr2 if x in set_arr1]


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = [0, 1, 3, 7]

    print(get_intersection(A, B))  # [1, 3]

    C = [1, 2, 2, 1]
    D = [2, 2]
    print(get_intersection(C, D))  # [2]