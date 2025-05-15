'''
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequencyof at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

'''

class Solution:
    # def combinationSum(self, candidates, target):
    #     res = []
        
    #     def dfs(i, cur, total):
    #         if total == target:
    #             res.append(cur.copy())
    #             return
    #         if i >= len(candidates) or total > target:
    #             return
            
    #         cur.append(candidates[i])
    #         dfs(i, cur, total + candidates[i])
    #         cur.pop()
    #         dfs(i+1, cur, total)
        
    #     dfs(0, [], 0)
    #     return res
    
    def combinationSum(self, candidates, target):
        # Time complexity: O(N^(M/min_cand + 1)), N = len(candidates), M = target, min_cand = min(candidates)
        # Space complexity: O(M/min_cand)
        def backtrack(index, curr_comb, curr_sum):
            if curr_sum == target:
                result.append(curr_comb)
                return
            
            if curr_sum > target:
                return

            for i in range(index, len(candidates)):
                backtrack(i, curr_comb + [candidates[i]], curr_sum + candidates[i])
        
        result = []
        backtrack(0, [], 0)
        return result

a = Solution().combinationSum(candidates = [2,3,6,7], target = 7)
print(a)

'''
Medium
#Array
#Backtracking
'''