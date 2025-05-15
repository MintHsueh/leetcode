'''
322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

'''

class Solution:
    # Recursion
    # Time Limit Exceeded
    def coinChange(self, coins, amount: int) -> int:
        def helper(idx, lenth, curr_sum):
            if curr_sum == amount:
                self.result = min(self.result, lenth)
                return
            
            if curr_sum > amount:
                return
            
            for i in range(idx, len(coins)):
                helper(i, lenth + 1, curr_sum + coins[i])


        self.result = amount + 1
        helper(0, 0, 0)    
        
        if self.result == amount + 1:
            return -1 
        return self.result
    
    # ***
    # DP
    # TC:m = O(mn). M= length of the coins array, n = amount
    # SC: O(n)
    def coinChange(self, coins, amount: int) -> int:
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0 # min_coins[amount] = the min numbers of coins can achieve amount

        for a in range(amount + 1):
            for coin in coins:
                if coin <= a:
                    min_coins[a] = min(min_coins[a], min_coins[a - coin] + 1)
            
        if min_coins[amount] == amount + 1:
            return -1
        return min_coins[amount]
    
'''
Medium
# Array
# Dynamic Programming
# Breadth-First Search
'''

