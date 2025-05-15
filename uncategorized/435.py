'''
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 
Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104

'''

class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        pre_idx = 0

        for idx in range(1, len(intervals)):
            if intervals[idx][0] < intervals[pre_idx][1]:   # 代表有重疊
                count += 1
            else:
                pre_idx = idx
        
        return count

'''
Medium
# Array
# Dynamic Programming
# Greedy
# Sorting
'''