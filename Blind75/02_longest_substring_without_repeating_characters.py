def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    left = 0
    ans = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        ans = max(ans, right - left + 1)
    return ans


if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
