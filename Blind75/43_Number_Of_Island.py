from typing import List


class Soultion:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1:
            return 0
        row_len = len(grid)
        col_len = len(grid[0])
        islands = 0

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1":
                    self.find(r, c, grid)
                    islands += 1
        return islands

    def find(self, r, c, grid):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if grid[r][c] == "1":
            grid[r][c] = "0"
            self.find(r - 1, c, grid)
            self.find(r + 1, c, grid)
            self.find(r, c - 1, grid)
            self.find(r, c + 1, grid)


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    object = Soultion()
    print(object.numIslands(grid))
