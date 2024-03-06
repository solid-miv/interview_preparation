# brute force; O(min(n,m)*log(max(n,m))); where n - the number of rows, m - the number of columns;
def sorted_matrix_search(arr: list[list[int]], target: int) -> tuple:
    """
    Search for a target integer in a sorted matrix of integers. Both rows and columns are sorted.

    Args:
        arr (list[list[int]]): A sorted matrix of integers.
        target (int): The integer to search for.
    
    Returns:
        tuple: The row and column indices of the target integer in the matrix, -1 if not found.
    """
    for i in range(len(arr)):
        if len(arr) <= len(arr[i]):
            if arr[i][0] <= target <= arr[i][-1]:
                low = 0
                high = len(arr[i]) - 1

                while low <= high:
                    mid = (low + high) // 2

                    if arr[i][mid] == target:
                        return (i, mid)
                    elif arr[i][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
        else:
            if arr[0][i] <= target <= arr[-1][i]:
                low = 0
                high = len(arr[0]) - 1

                while low <= high:
                    mid = (low + high) // 2

                    if arr[mid][i] == target:
                        return (mid, i)
                    elif arr[mid][i] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
    
    return -1

# O(n*log(m) + m*log(n)); where n - the number of rows, m - the number of columns;
# algorithm reduces O(n) and O(m) to O(n/4) and O(m/4) approxiamtely by using the central element of the matrix;
def sorted_matrix_search_2(arr: list[list[int]], target: int) -> tuple:
    """
    Search for a target integer in a sorted matrix of integers. Both rows and columns are sorted.

    Args:
        arr (list[list[int]]): A sorted matrix of integers.
        target (int): The integer to search for.
    
    Returns:
        tuple: The row and column indices of the target integer in the matrix, -1 if not found.
    """
    central_element_row = (len(arr) - 1) // 2
    central_element_col = (len(arr[0]) - 1) // 2

    possible_rows = []
    possible_cols = []

    if arr[central_element_row][central_element_col] == target:
        return (central_element_row, central_element_col)
    elif arr[central_element_row][central_element_col] < target:
        possible_rows.extend(list(range(central_element_row+1, len(arr))))
        possible_cols.extend(list(range(central_element_col+1, len(arr[0]))))
    else:
        possible_rows.extend(list(range(0, central_element_row)))
        possible_cols.extend(list(range(0, central_element_col)))

    for i in possible_cols:
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid][i] == target:
                return (mid, i)
            elif arr[mid][i] < target:
                low = mid + 1
            else:
                high = mid - 1
        
    for i in possible_rows:
        low = 0
        high = central_element_col - 1

        while low <= high:
            mid = (low + high) // 2
        
            if arr[i][mid] == target:
                return (i, mid)
            elif arr[i][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

    return -1


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [3, 5, 6, 7],
              [4, 10, 12, 15],
              [5, 11, 13, 18],
              [6, 12, 16, 19],
              [8, 13, 17, 20]]

    
    answ = sorted_matrix_search_2(matrix, 12)
    print(answ)