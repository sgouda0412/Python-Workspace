def power_of_a_number(p, n):
    # return pow(p, n)

    if n == 0:
        return 1
    t = power_of_a_number(p, n // 2)
    t = t * t

    if n % 2 == 0:
        return t
    else:
        return t * p


if __name__ == "__main__":
    p = 3
    n = 9
    print(power_of_a_number(p, n))
