from typing import List
import pysnooper

@pysnooper.snoop()
def maxProfit(prices: List[int]) -> int:
    l = 0
    r = 1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
        else:
            l = r
        r = r + 1
    return max_profit


if __name__ == "__main__":
    #prices = [7, 1, 5, 3, 6, 4]
    prices = [7,6,4,3,1]
    print(maxProfit(prices))
