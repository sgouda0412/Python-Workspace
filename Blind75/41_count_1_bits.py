def hammingWeight(n: int) -> int:
    ans = 0
    while n:
        ans += n % 2
        n = n >> 1
    return ans

if __name__ == "__main__":
    n = 7
    print(hammingWeight(n))