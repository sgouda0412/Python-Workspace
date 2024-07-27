def reverseBits(n: int) -> int:
    ans = 0

    for i in range(32):
        b = (n >> i ) & 1
        ans += (b << (31 - i))
    return ans


if __name__ == "__main__":
    n = 43261596
    print(reverseBits(n))