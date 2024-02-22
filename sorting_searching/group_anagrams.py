from collections import defaultdict, Counter


#O(n*k*log(k)); n - length of the list, k - max length of the string
def group_anagrams(arr: list[str]) -> list[str]:
    """Groups anagrams together.

    Args: 
        arr (list): The list of original strings.
    
    Returns:
        list: The list of grouped anagrams.
    """

    table = {}
    count = 0

    for item in arr:
        list_item = list(item)
        list_item.sort()
        list_item = "".join(list_item)

        if list_item in table:
            tpl = table[list_item]
            tpl += (count,)
            table[list_item] = tpl
        else:
            table[list_item] = (count,)

        count += 1

    answ = []

    for value in table.values():
        for i in range(len(value)):
            answ.append(arr[value[i]])

    return answ

# O(n^2); n - length of the list
def group_anagrams_modified(arr: list[str]) -> list[str]:
    """Groups anagrams together.

    Args: 
        arr (list): The list of original strings.
    
    Returns:
        list: The list of grouped anagrams.
    """

    table = {}

    for item in arr:
        char_table = {}

        for c in item:
            char_table[c] = 1 if c not in char_table else char_table[c] + 1
            
        table[item] = char_table

    answ = []

    for value in table.values():
        for i in range(len(arr)):
            if table[arr[i]] == value:
                answ.append(arr[i])

        if len(arr) == len(answ):
            break    
    
    return answ

#O(n*k*log(k)); n - length of the list, k - max length of the string
def group_anagrams_modified2(arr: list[str]) -> list[str]:
    """Groups anagrams together.

    Args: 
        arr (list): The list of original strings.
    
    Returns:
        list: The list of grouped anagrams.
    """

    table = defaultdict(list)

    for item in arr:
        chars = Counter(item)
        chars_tuple = tuple(sorted(chars.items()))  # sorting takes O(k*log(k))
        
        table[chars_tuple].append(item)
    
    answ = []

    for key in table.keys():
        answ.extend(table[key])

    return answ


if __name__ == "__main__":
    arr = ["nkl", "hello", "aba", "olleh", "baa", "kln"]

    x = group_anagrams_modified2(arr)

    print(x)