import re
def isPalindrome(s: str) -> bool:
    s = re.sub("[^a-z|^0-9]","",s.lower())
    l = 0
    r = len(s)- 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))