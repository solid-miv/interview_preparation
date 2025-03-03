from heapq import heappush, heappop
from typing import List

# O(n*logn) time complexity
def get_3_closest_points(points: List[List[int]], k: int):
    def get_dist(x, y):
        return x ** 2 + y ** 2
    
    min_heap = []

    for i in range(len(points)):
        x, y = points[i]
        heappush(min_heap, (get_dist(x, y), points[i]))

    result = []

    for _ in range(k):
        result.append(heappop(min_heap)[1])
    
    return result


if __name__ == "__main__":
    A = [[2, -1], [3, 2], [4, 1],
         [-1, -1], [-2, -2]]
    print(get_3_closest_points(A, 3))  # [[-1, -1], [2, -1], [-2, -2]]