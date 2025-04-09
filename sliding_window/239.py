# 239. Sliding Window Maximum
# Hard
# 2025/04/10 好難QQ

from collections import deque
class Solution:
    # key: 用遞減 deque, 維持 deque 最前面永遠是目前視窗內的最大值
    # TC: O(n), SC: O(k) 因為 deque 最多只會存下 k 個 index（視窗大小）
    def maxSlidingWindow(self, nums, k):
        dq = deque() # dq 裡放 index
        result = []

        for i in range(len(nums)):
            # 保持 dq 裡的 index 對應的數字為遞減 (當之前的數字比當前的小，那些之前的數字就不用考慮了，他們不可能會是最大值)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            # 當視窗內數字個數超過 k 個，要把第一個刪掉
            if dq[0] == i-k:
                dq.popleft() 

            # 一旦視窗形成（至少 k 個數字），就要每次都加入最大值（最前面的 index）
            if i >= k-1:
                result.append(nums[dq[0]])
        
        return result

       
    # 暴力解
    # TC: O(n * k) 爆掉嗚嗚
    def maxSlidingWindow_BF(self, nums, k):
        result = []
        for l in range(len(nums)-k+1):
            result.append(max(nums[l:l+k]))
        return result

'''
Notes:

解題思路:

遍歷 nums:
    1. 從 deque 尾端往前, 依序跟當前數字比大小, 若 deque 最後一個數字較小, 就 pop 掉（因為永遠不可能成為最大） → 保持 deque[0] 的數字為視窗內的最大值
    2. 把目前數字加入 deque 的最後面
    3. 判斷最前面那個數字是不是不在視窗內了, 如果是就踢掉
    4. 最前面的就是目前這個視窗的最大值, append 到結果

'''

