# def gcd(numbers):
#     def compute_gcd(a, b):
#         while b:
#             r = a % b
#             a = b
#             b = r
#         return a
#     g = numbers[0]
#     for num in numbers[1:]:
#         g = compute_gcd(num, g)
#     return g


# if __name__ == "__main__":
#     numbers = [8, 16, 24, 27]
#     print(gcd(numbers))

# import concurrent.futures
# import math
# import itertools

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# def prime_checker(numbers):
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         results = executor.map(is_prime, numbers)
#     return [n for n, prime in zip(numbers, results) if prime]

# def main():
#     big_numbers = iter([112272535095293, 112582705942171, 112272535095293,
#                         115280095190773, 115797848077099, 1099726899285419, 2, 3])
#     while True:
#         chunk = list(itertools.islice(big_numbers, 1000))
#         if not chunk:
#             break
#         primes = prime_checker(chunk)
#         for prime in primes:
#             print(f"Prime: {prime}")

# if __name__ == "__main__":
#     main()

# import concurrent.futures
# import math

# PRIMES = [
#     112272535095293,
#     112582705942171,
#     112272535095293,
#     115280095190773,
#     115797848077099,
#     1099726899285419
# ]

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# def main():
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         results = executor.map(is_prime, PRIMES)
#     for result in results:
#         print(f"Prime: {result}")

# if __name__ == "__main__":
#     main()

l = ["santosh", "is", "great"]
print("-".join(l))

# import operator

# numbers = [1, 2, 3, 4, 5]
# product = operator.mul(*numbers)
# print(product)

my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]

s = sorted(people, key=lambda x: x["age"], reverse=True)
print(s)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = slice(0, len(nums), 2)
print(nums[s])


author = "santosh"
print(f"Example 1: {author}")
print(f"Example 2: {2 + 2}")

pi_val = 3.141592

print(f"Example 1: {pi_val:f}")
print(f"Example 2: {pi_val:.0f}")
print(f"Example 3: {pi_val:.1f}")
print(f"Example 4: {pi_val:.3f}")

# https://medium.com/geekculture/python-f-string-codes-i-use-every-day-e03558f12057

# lib(pakages, modules) -> package(multiple modules, __init__.py) -> modules(functions)
# scripts(outside of libraries)
# import pandas  # type: ignore
# import os
