def initialize_window(sequence, window_size):
    window = sequence[:window_size]
    return window


# Example usage:
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 3

initial_window = initialize_window(sequence, window_size)
print("Initial Window:", initial_window)

# -----------------------------------------------------------


def move_window(sequence, window, current_index):
    # Remove the leftmost element from the window
    window.pop(0)

    # Add the next element to the window
    window.append(sequence[current_index])

    return window


# Example usage:
sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 3

# Initialize the window
current_window = sequence[:window_size]
print("Initial Window....:", current_window)

# Move the window through the sequence
for i in range(window_size, len(sequence)):
    current_window = move_window(sequence, current_window, i)
    print("Window at index", i, ":", current_window)


# ----------------------------------------------------------------


def max_sum_subarray(nums, k):
    if len(nums) < k:
        return
    current_sum = max_sum = sum(nums[:k])

    for i in range(0, len(nums) - k):
        current_sum = current_sum - nums[i] + nums[i + k]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    K = 3
    print(max_sum_subarray(arr, K))

# -------------------------------------------------------------------
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    l = r = current_sum = 0
    min_len = float("inf")

    for r in range(len(nums)):
        current_sum += nums[r]
        while current_sum >= target:
            min_len = min(min_len, r - l + 1)
            current_sum = current_sum - nums[l]
            l += 1
        r += 1
    return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]

    print(minSubArrayLen(target, nums))

# ----------------------------------------------------------------------

# https://www.geeksforgeeks.org/find-length-of-the-longest-subarray-containing-atmost-two-distinct-integers/

# Question:     subarray target value index range


class Solution:
    def subArraySum(self, arr, n, s):
        # Write your code here
        curSum = 0
        left = 0
        right = 0
        while right < n:
            curSum += arr[right]
            while curSum > s and left < right:
                curSum -= arr[left]
                left += 1
            if curSum == s:
                return [left + 1, right + 1]
            right += 1
        return [-1]


if __name__ == "__main__":
    o = Solution()
    n = 5
    s = 12
    arr = [1, 2, 3, 7, 5]
    print(o.subArraySum(arr, n, s))


# ---------------------------------------------------------------------------------------

# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold


def numOfSubarrays(arr, k, threshold):
    required_sum = k * threshold
    current_sum = sum(arr[:k])
    count = 0

    if current_sum >= required_sum:
        count += 1

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        if current_sum >= required_sum:
            count += 1

    return count


# Example usage:
arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
print(numOfSubarrays(arr, k, threshold))  # Output: 3

# -------------------------------------------------------------------------------------


from collections import Counter


def find_anagrams(s, p):
    len_s, len_p = len(s), len(p)
    if len_s < len_p:
        return []

    p_count = Counter(p)
    s_count = Counter()
    result = []

    left = 0
    for right in range(len(s)):
        s_count[s[right]] += 1

        if right >= len(p):
            if s_count[s[left]] == 1:
                del s_count[s[left]]
            else:
                s_count[s[left]] -= 1
            left += 1

        if s_count == p_count:
            result.append(left)

    return result


# Example usage
s = "cbaebabacd"
p = "abc"
print(find_anagrams(s, p))  # Output: [0, 6]
