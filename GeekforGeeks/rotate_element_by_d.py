from typing import List


class Solution:
    def rotateArr(self, A: List[int], D: int, N: int):
        D %= N
        A[:] = A[D:] + A[:D]
        return A


if __name__ == "__main__":
    obj: Solution = Solution()
    n: int = 5
    d: int = 2
    arr: List[int] = [1, 2, 3, 4, 5]
    print(obj.rotateArr(arr, d, n))
