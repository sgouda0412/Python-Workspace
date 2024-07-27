def ispal(n):
    rev = 0
    temp = n

    while temp != 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp //= 10
    return rev == n


def _reverse(m):
    rev = 0
    while m > 0:
        ld = m % 10
        rev = rev * 10 + ld
        m //= 10
    return rev


if __name__ == "__main__":
    n = 121
    m = 12345
    print(ispal(n))
    print(_reverse(m))
