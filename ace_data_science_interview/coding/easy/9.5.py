from typing import List


def find_largest_subsum(arr: List[int]) -> int:
    max_sum = arr[0]
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(find_largest_subsum(arr))  # 6