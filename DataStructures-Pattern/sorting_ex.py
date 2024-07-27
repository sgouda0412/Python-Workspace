# bubble sort works best when array is nearly sorted..
def swap(a, b):
    a, b = b, a

def bubble_sort(nums):
    for i in range(0, len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key
    return nums


# insertion sort ->  everytime insert the card at the right position

def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_idx = i 
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        swap(nums[min_idx], nums[i])
        
    return nums
def merge_sort(nums):
    pass

def quick_sort(nums):
    pass


if __name__ == "__main__":
    nums = [5, 6, 4, 8, 9, 2]
    print(bubble_sort(nums))
    print(insertion_sort(nums))
    print(selection_sort(nums))
    print(merge_sort(nums))
    print(quick_sort(nums))
    
