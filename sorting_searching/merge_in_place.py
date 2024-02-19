def sorted_merge(a: list, b: list, len_a: int, len_b: int) -> None:
    """Merges two sorted lists in a single sorted one (one of the given lists has enough buffer to hold the second list).

    Args:
        a (list): The first sorted list with enough buffer to hold the second list.
        b (list): The second sorted list.
        len_a (int): Length of the first list.
        len_b (int): Length of the second list.

    Returns:
        None: Function works in-place.
    """
    last_a = len_a - 1
    last_b = len_b - 1
    last_merged = len_a + len_b - 1

    while last_b >= 0:
        if last_a >= 0 and a[last_a] > b[last_b]:
            a[last_merged] = a[last_a]
            last_a -= 1
        else:
            a[last_merged] = b[last_b]
            last_b -= 1
        
        last_merged -= 1
    

if __name__ == "__main__":
    arr1 = [-3, 4, 7, 21, 0, 0, 0, 0]
    arr2 = [-20, -2, 5, 8]

    sorted_merge(arr1, arr2, len(arr1)-len(arr2), len(arr2))

    print(arr1)