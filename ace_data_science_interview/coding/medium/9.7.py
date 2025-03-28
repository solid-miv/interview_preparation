from typing import List


def get_peak_index(arr: List[int]) -> int:
    start, end = 0, len(arr) - 1

    while True:
        mid = (start + end) // 2

        left = arr[mid - 1] if mid - 1 >= 0 else float("-inf")
        right = arr[mid + 1] if mid + 1 < len(arr) else float("-inf")

        if left < arr[mid] and right < arr[mid]:
            return mid
        elif right > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        