"""
Given two lists X and Y, return their correlation.
"""
import math
from typing import List

def mean(lst: List[float]) -> float:
    return sum(lst) / len(lst)


def stddev(lst: List[float]) -> float:
    mean_lst = mean(lst)

    return math.sqrt(sum((x - mean_lst) ** 2 for x in lst) / len(lst))


def covariance(x: List[float], y: List[float]) -> float:
    assert len(x) == len(y), "Lists must be of the same length"

    mean_x = mean(x)
    mean_y = mean(y)

    return sum((x_i - mean_x) * (y_i - mean_y) for x_i, y_i in zip(x, y)) / len(x)

# O(n)- time complexity
def correlation(X: List[float], Y: List[float]) -> float:
    assert len(X) == len(Y), "Lists must be of the same length"

    return covariance(X, Y) / (stddev(X) * stddev(Y))


if __name__ == "__main__":
    X = [1, 2, 3, 4, 5]
    Y = [-1, -2, -3, -4, -5]

    print(correlation(X, Y))  # tutput: 0.99