from collections.abc import Sequence, Callable, Container

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(isinstance(l, Sequence))


from typing import Callable


def apply_function(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


print(apply_function(add, 2, 3))  # Output: 5
print(apply_function(multiply, 2, 3))  # Output: 6


from collections.abc import Sequence, Mapping


class Flower:
    def __init__(self, name):
        self.name = name


def deliver_bouquet(bouquets: Sequence[Flower], address: Mapping[Flower, str]):
    for bouquet in bouquets:
        deliver_address = address.get(bouquet)
        print(f"Delivering {bouquet.name} to {deliver_address}")


f1 = Flower("Hyacinth")
f2 = Flower("Forsythia")
flowers = [f1, f2]
address = {
    f1: "Mary Doe, 123 Telegraph Avenue, Oakland CA",
    f2: "John Cena, 456 MLK Road, Elcerrito CA",
}

deliver_bouquet(flowers, address)


from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")  # declare type variable


def last(s: Sequence[T]) -> T:
    return s[len(s) - 1]


# https://www.youtube.com/watch?v=oJd6lhF0JbI&t=24s

from typing import Generic, TypeVar, TypedDict
