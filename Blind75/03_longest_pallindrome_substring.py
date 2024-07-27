def longestPalindrome(s):
    def expand_around_center(left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    res = ""
    for i in range(len(s)):
        res = max(
            expand_around_center(i, i), expand_around_center(i, i + 1), res, key=len
        )

    return res


if __name__ == "__main__":
    s = "babad"
    print(longestPalindrome(s))
