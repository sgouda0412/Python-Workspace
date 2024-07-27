def uniquePaths(m: int, n: int) -> int:
    # if m == 1 or n == 1:
    #     return 1
    # return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


if __name__ == "__main__":
    m = 3
    n = 7
    print(uniquePaths(m, n))
