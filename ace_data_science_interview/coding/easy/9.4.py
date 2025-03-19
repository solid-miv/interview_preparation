from heapq import heappush, heappop  # heapq uses min heap by default
from typing import List

# O(k^2*log(k)) time complexity (if k << len(arr))
def get_kth_smallest(arr: List[List[int]], k: int):
    heap = []
    res = -1

    for i in range(min(k, len(arr))):
        for j in range(min(k, len(arr))):
            heappush(heap, arr[i][j])

    for _ in range(k):
        res = heappop(heap)
    
    return res


if __name__ == "__main__":
    A = [[1, 4, 7],
         [3, 5, 9],
         [6, 8, 11]]
    print(get_kth_smallest(A, 6))