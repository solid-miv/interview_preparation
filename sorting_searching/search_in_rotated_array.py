# O(log(n)) - on average, O(n) - worst case; n- length of the list
def search_in_rotated_list(arr: list[int], target: int) -> int:
    """
    Search for a target in a rotated unknown times list. The list is rotated at an unknown pivot.
    
    Args:
        arr (list): a list of integers.

        target (int): the target to search for in the list.
    
    Returns:
        int: the index of the target in the list, -1 if not found.
    """
    i, j = 0, 1

    while arr[i] <= arr[j] and j < len(arr)-1:
        i += 1
        j += 1

    if arr[i] > target and arr[0] <= target:
        low = 0
        high = i

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
    else:
        low = j
        high = len(arr) - 1

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
    x = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14, 15]
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    z = [2, 2, 2, 2, 2, 3, 4, 2]

    answer = search_in_rotated_list(z, 2)

    print(answer)