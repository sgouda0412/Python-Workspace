# class Solution:
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    l = 0
    r = len(matrix[0])
    t = 0
    b = len(matrix)
    ans = []
    while l < r and t < b:
        for i in range(l, r):
            ans.append(matrix[t][i])

        t += 1

        for i in range(t, b):
            ans.append(matrix[i][r - 1])
        r -= 1

        if not (l < r and t < b):
            break

        for i in range(r - 1, l - 1, -1):
            ans.append(matrix[b - 1][i])
        b -= 1

        for i in range(b - 1, t - 1, -1):
            ans.append(matrix[i][l])
        l += 1
    return ans


if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder(matrix))

#Output: [1,2,3,6,9,8,7,4,5]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]