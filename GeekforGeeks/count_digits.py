def count_digits(n: int):
    res = 0
    while n > 0:
        n //= 10
        res += 1
    return res


if __name__ == "__main__":
    n: int = 346776514
    print(count_digits(n))
