'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45

'''

class Solution:
    # recursive 
    # TC: O(2^n)
    # SC: O(n)
    # Time Limit Exceeded
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    #***
    # Dynamic programming
    # TC: O(n).As we are traversing the vector atleast 1 time.
    # SC: O(n). Array of size n
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        if n <= 2:
            return n

        steps = {1:1, 2:2}
        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]
        
        return steps[n]
    
    # Iterative
    # TC: O(n)
    # SC: O(1)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev, prev2 = 2, 1
        for i in range(3, n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        
        return curr

'''
Easy
# Math
# Dynamic Programming
# Memoization
'''