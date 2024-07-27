"""_summary_
"""

def is_prime(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_prime_numbers(limit):
    """_summary_

    Args:
        limit (_type_): _description_
    """
    prime_numbers = []
    for num in range(limit + 1):
        if is_prime(num):
            prime_numbers.append(num)
    print(prime_numbers)


# Example usage
if __name__ == "__main__":
    LIMIT_PRIME_NUMBER = 100
    print_prime_numbers(LIMIT_PRIME_NUMBER)
