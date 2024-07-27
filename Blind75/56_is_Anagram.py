from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    #return sorted(s) == sorted(t)
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "caracer"
    t = "racecar"

    print(isAnagram(s, t))
 