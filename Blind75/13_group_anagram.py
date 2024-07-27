from typing import List

# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     d = {}

#     for word in strs:
#         sorted_word = "".join(sorted(word))
#         print(sorted_word)
#         if sorted_word not in d:
#             d[sorted_word] = [word]
#         else:
#             d[sorted_word].append(word)

#     result = []

#     for item in d.values():
#         result.append(item)
#     return result

# if __name__ == "__main__":
#     strs = ["eat","tea","tan","ate","nat","bat"]
#     print(groupAnagrams(strs))


# from typing import List
# from collections import defaultdict


# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     grouped_anagrams = defaultdict(list)

#     for each_str in strs:
#         # Sort the string
#         sorted_str = "".join(sorted(each_str))
#         # Append the original string to the list of the sorted string key
#         grouped_anagrams[sorted_str].append(each_str)

#     return list(grouped_anagrams.values())


# if __name__ == "__main__":
#     strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#     print(groupAnagrams(strs))

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for c in strs:
            ss = "".join(sorted(c))
            d[ss].append(c)
        return list(d.values())


x = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(x.groupAnagrams(strs))
