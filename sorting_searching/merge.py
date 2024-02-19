def merge(arr1: list, arr2: list) -> list:
    """Merges two sorted lists in a single sorted list.
    
    Args:
        arr1 (list): The first sorted list.
        arr2 (list): The second sorted list.

    Returns:
        list: Merged combination of arr1 and arr2. 
    """

    answ = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            answ.append(arr1[i])
            i += 1
        else:
            answ.append(arr2[j])
            j += 1
        
    while i < len(arr1):
        answ.append(arr1[i])
        i += 1

    while j < len(arr2):
        answ.append(arr2[j])
        j += 1
    
    return answ


if __name__ == "__main__":
    x = merge([-3, 10, 45], [-10, 5, 13, 22, 78])
    print(x)