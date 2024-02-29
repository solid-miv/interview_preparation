# worst case O(n) if the array consists of empty strings; average case of O(log(n)); n - the length of the array;
def sparse_search(arr: list[str], target: str) -> int:
    """
    Search for a string in a sorted array of strings that is interspersed with empty strings.

    Args:
        arr (list[str]): A sorted array of strings interspersed with empty strings.
        target (str): The string to search for.
    
    Returns:
        int: The index of the target string in the array, -1 if not found.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif len(arr[mid]) != 0 and arr[mid] < target:
            low = mid + 1
        elif len(arr[mid]) != 0 and arr[mid] > target:
            high = mid - 1
        else:
            while len(arr[mid]) == 0 and mid >= 1:
                mid -= 1

            if arr[mid] == target:
                return mid
            elif arr[mid] < target and (low - mid) != 1:  # (low - mid) != 1 is to avoid infinite loop
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                return -1  
            
    return -1


if __name__ == "__main__":
    x = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    answ = sparse_search(x, "ball")
    print(answ)
    answ = sparse_search(x, "dad")
    print(answ)
    answ = sparse_search(x, "at")
    print(answ)
    answ = sparse_search(x, "car")
    print(answ)
    answ = sparse_search(x, "dad")
    print(answ)