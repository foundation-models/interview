from typing import List
from unittest import main, TestCase

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = prices[0]
        total_profit = 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit = prices[i] - x
            else:
                total_profit += profit
                profit = 0
                x = prices[i]
        total_profit += profit
        return total_profit
 
        
if __name__ == "__main__":
    x = Solution()
    # assert(x.merge([], 0, [], 0) == [])
    # assert(x.merge([0], 1, [1], 1) == [1])
    assert(x.maxProfit([7,1,5,3,6,4]) == 7)


