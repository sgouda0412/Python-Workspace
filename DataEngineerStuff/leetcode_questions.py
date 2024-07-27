# https://medium.com/@learntocodetoday/100-top-coding-questions-prepare-for-faang-interviews-like-a-pro-3df5addc8a64

# https://singhneeruk.medium.com/top-20-dsa-coding-patterns-79e3ce67d098

# https://medium.com/enjoy-algorithm/popular-problem-solving-approaches-in-data-structures-and-algorithms-6b4d30a0823d


# https://medium.com/@humzanaveed/neetcode-leetcode-python-solutions-of-arrays-hashing-problems-with-descriptions-22695928dc3e

# https://medium.com/@humzanaveed/neetcode-leetcode-python-solutions-of-two-pointers-problems-e762ce5528f0


from typing import List


# def twoSum(nums: List[int], target: int) -> List[int]:
#     lookup = {}

#     for index, value in enumerate(nums):
#         diff = target - value

#         if diff in lookup:
#             return [lookup[diff], index]

#         lookup[value] = index

#     return [-1, -1]


# if __name__ == "__main__":
#     nums = [2, 8, 9, 13]
#     target = 9
#     print(twoSum(nums, target))

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# def groupAnagrams(strs: List[str]) -> List[List[str]]:
# lookup = {}

# for str in strs:
#     s_str = "".join(sorted(str))
# if s_str in lookup:
#     lookup[s_str].


# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     grouped_anagrams = {}

#     for str_ in strs:
#         # sort the string
#         s_str_ = "".join(sorted(str_))
#         print(s_str_)
#         # if sorted string key exists append the original string
#         if s_str_ in grouped_anagrams:
#             grouped_anagrams[s_str_].append(str_)
#         else:
#             # Create a key-value pair with sorted string as key
#             #  and original string as value
#             grouped_anagrams[s_str_] = [str_]
#     return list(grouped_anagrams.values())


# if __name__ == "__main__":
#     strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#     print(groupAnagrams(strs))


from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    grouped_anagrams = defaultdict(list)

    for str_ in strs:
        # Sort the string
        s_str_ = "".join(sorted(str_))
        # Append the original string to the list of the sorted string key
        grouped_anagrams[s_str_].append(str_)

    return list(grouped_anagrams.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
