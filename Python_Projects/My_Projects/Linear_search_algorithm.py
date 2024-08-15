def linear_search(list, target):
    '''
    Returns index of target if found, else returns None
    '''
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not found...")
        
numbers = list(range(10))
result1 = linear_search(numbers, 8)
result2 = linear_search(numbers, 12)
verify(result1)
verify(result2)
