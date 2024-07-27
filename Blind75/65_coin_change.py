from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    # if amount == 0:
    #     return 0
    # dp = [float('inf') for _ in range(amount)]
    # dp = [0] + dp
    # for i in range(amount + 1):
    #     for coin in coins:
    #             # print(i, coin, dp)
    #         if i >= coin:
    #             dp[i] = min(dp[i], dp[i - coin] + 1)
    # return dp[-1] if dp[-1] < float('inf') else -1

    if amount == 0:
        return 0
    if amount < 0:
        return -1
    
    min_coins = float("inf")

    for coin in coins:
        res = coinChange(coins, amount - coin)
        if res >= 0 and res < min_coins:
            min_coins = res + 1
    return min_coins if min_coins != float('inf') else  -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))