def binary_search(list, target):
    first = 0
    list.sort()
    last = len(list) - 1
    while first <= last:
        mid = (first + last) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        elif list[mid] > target:
            last = mid - 1
    
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print("Target not found...")

numbers = [3, 4, 2, 7, 9, 8, 6, 10, 1, 5]
result1 = binary_search(numbers, 4)
result2 = binary_search(numbers, 12)
print(result1)
print(result2)
