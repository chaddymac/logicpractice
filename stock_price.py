from cgitb import small
from typing import *
## prices always greater than 1
## Always have to buy before sale
## [5,4,3,2,1] = 0 
## [[7,1,5,3,6,4]] = 5 buy at 1 sell at 6
## [[2,7,1,5,3,4]] = 5 buy at 2 sell at 7
## [[5,8,1,2,2,6]] = 5

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small_num = 10**4
        final = 0 

        for price in prices:
            if price < small_num:
                small_num = price
            elif final < (price - small_num):
                final = price - small_num
        return final
            

l1 = [5,4,3,2,1]
l2 = [7,1,5,3,6,4]
l3 = [5,8,1,2,2,6]

solution = Solution()
print(solution.maxProfit(l3))