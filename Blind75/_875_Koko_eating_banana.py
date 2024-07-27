from typing import List
import math


def minEatingSpeed(piles: List[int], h: int) -> int:
    def f(piles, speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours

    left, right = 1, max(piles) + 1
    while left < right:
        speed = left + (right - left) // 2
        hours = f(piles, speed)
        if hours > h:
            left = speed + 1
        elif hours < h:
            right = speed
        elif hours == h:
            right = speed
    return left


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(minEatingSpeed(piles, h))
