from typing import List

def rotate(matrix: List[List[int]]) -> None:
    N = len(matrix)

    for i in range(N):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in matrix:
        i.reverse()
    
    return matrix

if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
            ]
    print(rotate(matrix))