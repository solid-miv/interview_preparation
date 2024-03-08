# O(n); n - the length of the array
def peaks_valleys(arr: list[int]) -> None:
    """
    Arranges the elements of the array in-place such that peaks and valleys alternate.

    Args:
        arr (list[int]): The array to be arranged.

    Returns:
        None: The array is arranged in-place.
    """
    def max_index(arr, a, b, c):
        length = len(arr)

        a_val = arr[a] if a >= 0 and a < length else float("-inf")
        b_val = arr[b] if b >= 0 and b < length else float("-inf")
        c_val = arr[c] if c >= 0 and c < length else float("-inf")

        max_val = max(a_val, b_val, c_val)

        if a_val == max_val:
            return a
        elif b_val == max_val:
            return b
        else:
            return c

    for i in range(2, len(arr), 2):
        biggest_index = max_index(arr, i-1, i, i+1)

        if i != biggest_index:
            arr[i], arr[biggest_index] = arr[biggest_index], arr[i]


# O(n); n - the length of the array
def peaks_valleys_2(arr: list[int]) -> None:
    """
    Arranges the elements of the array in-place such that peaks and valleys alternate.

    Args:
        arr (list[int]): The array to be arranged.

    Returns:
        None: The array is arranged in-place.
    """
    for i in range(2, len(arr)-1, 2):
        a = arr[i-1]
        b = arr[i]
        c = arr[i+1]

        max_in_triple = max(a, b, c)

        if max_in_triple == a:
            a, b = b, a
        elif max_in_triple == c:
            b, c = c, b
        
        arr[i-1] = a
        arr[i] = b
        arr[i+1] = c


if __name__ == "__main__":
    arr = [8, 3, 1, 2, 4, 6, 5, 7, 9, 10]
    # arr = [5, 3, 1, 2, 3]
    peaks_valleys_2(arr)
    print(arr)