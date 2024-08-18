def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        list.sort()
        mid = (len(list)) // 2
        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid+1:], target)
            else:
                return recursive_binary_search(list[:mid], target)
            
def verify(result):
    print(f"Target found: {result}")

numbers = [2, 4, 9, 7, 3, 1, 5, 8, 10, 6]
result1 = recursive_binary_search(numbers, 5)
result2 = recursive_binary_search(numbers, 12)
verify(result1)
verify(result2)
