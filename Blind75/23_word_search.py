from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    def backtrack(r, c, i):
        if i == ln:
            return True
        for dr, dc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
            tmp, board[r][c] = board[r][c], "#"
            if 0 <= dr < m and 0 <= dc < n and board[dr][dc] == word[i]:
                if backtrack(dr, dc, i + 1):
                    return True
            board[r][c] = tmp

    m, n, ln = len(board), len(board[0]), len(word)
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if backtrack(i, j, 1):
                    return True
    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(exist(board, word))
