def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


# def iterative_fact(n):
#     res = 1

#     for i in range(2, n + 1):
#         res = res * i
#     return res


if __name__ == "__main__":
    n = 24  
    print(factorial(n))
    # print(iterative_fact(n))
