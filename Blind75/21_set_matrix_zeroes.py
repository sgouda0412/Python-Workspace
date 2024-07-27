#Practices again still not clear with the logics.....


# def setZeroes(matrix):
#     if not matrix or not matrix[0]:
#         return

#     rows, cols = len(matrix), len(matrix[0])
#     zero_rows, zero_cols = set(), set()

#     # Find the rows and columns with zeros
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0:
#                 zero_rows.add(i)
#                 zero_cols.add(j)

#     # Set entire rows to zero
#     for row in zero_rows:
#         for j in range(cols):
#             matrix[row][j] = 0

#     # Set entire columns to zero
#     for col in zero_cols:
#         for i in range(rows):
#             matrix[i][col] = 0

#     return matrix

def setZeroes(matrix):
    # trackers for which rows and cols to flip to 0s
    rows, cols = set(), set()
    m, n = len(matrix), len(matrix[0])
    # first go through the matrix and find all 0s
    for i in range(m):
        for j in range(n):
            # track which row and column
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    # go through each element in the trackers, change elements to 0s
    while rows:
        next_row = rows.pop()
        for i in range(n):
            matrix[next_row][i] = 0
    while cols:
        next_col = cols.pop()
        for i in range(m):
            matrix[i][next_col] = 0
    # not needed for leetcode, but we just return the original matrix
    return matrix
# Example usage:
matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

print(setZeroes(matrix))

# Output:
# [
#     [1, 0, 3],
#     [0, 0, 0],
#     [7, 0, 9]
# ]
