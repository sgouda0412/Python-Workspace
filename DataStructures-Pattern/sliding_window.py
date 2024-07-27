from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        lookup = {}

        for r in range(len(s)):
            lookup[s[r]] = 1 + lookup.get(s[r], 0)
            while (r - l + 1) - max(lookup.values()) > k:
                lookup[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans


if __name__ == "__main__":
    s = "ABAB"
    k = 2
    print(Solution().characterReplacement(s, k))
