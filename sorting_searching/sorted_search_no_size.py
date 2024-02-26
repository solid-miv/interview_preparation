# O(log(n)); n - length of the list
def sorted_search_no_size(arr: list[int], target: int) -> int:
    """
    Finds the index of the target in a list that can't return its length.

    Args:
        arr (list[int]): The list to search in. It can't return its length.

        target (int): The target to search for.
    
    Returns:
        int: The index of the target in the list, -1 if not found.
    """

    limit_ind = 2

    # find the upper capacity limit of the list
    while arr[limit_ind-1] != -1:
        limit_ind *= 2

    high = limit_ind - 1
    low = high // 2

    # find index of the last element in the list
    while arr[high] == -1:
        mid = (low + high) // 2

        if arr[mid] == -1:
            high = mid - 1
        else:
            low = mid

    low = 0  # reset low to 0

    # binary search
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, -1, -1]
    answ = sorted_search_no_size(x, 22)
    print(answ)