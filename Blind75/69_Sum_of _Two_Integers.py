def getSum(a: int, b: int) -> int:
    # while b != 0:
    #     temp = a
    #     a = temp ^ b
    #     b = (temp & b) << 1
    # return a
    if b == 0:
        return a
    sum = a ^ b
    carry = a & b << 1
    return getSum(sum, carry)


if __name__ == "__main__":
    a = 3
    b = 4
    print(getSum(a, b))
