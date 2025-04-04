# 4. Median of Two Sorted Arrays
# Hard
# 2025/04/05 好難QQ

class Solution:
    # TC: O(log(min(n,m))), SC: O(1)
    # key: 把兩個 arr 分成總共左右兩半，使左半邊的所有數字都 < 右半邊的所有數字，也就是「左半部最大值 ≤ 右半部最小值」
    # 等同於: 把兩個 arr 各自切半，讓 nums1_left ≤ nums2_right 且 nums2_left ≤ nums1_right
    
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        if len(nums1) > len(nums2):     # 對短 arr 做 binary search: 1.較快 2.若從長 arr 切割, 會有左右兩邊數量不一樣問題 (即下面的可避免 j 變成負數)
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left_total = (m + n + 1) // 2   # 左半邊要有的數字個數總和（總數偶數 → 左右一樣多；奇數 → 左邊多一個）

        left, right = 0, m      # nums1 切割線位置的範圍 (切點 i 有可能等於 m ，也就是切在最右邊)
        while left <= right:    # 當 left == right 時，還要再試一次那個切點 (如果只寫 <，會漏掉最後一次可能的切法)
            i = (left + right) // 2    # i 為 nums1 的切割線位置，代表切割線位於 index i-1 與 i 之間，也就是切割線左半邊有 i 個數字
            j = left_total - i         # 同上，j 為 nums2 切割線的位置，也就是切割線左半邊有 j 個數字，j = 左半邊總個數 - i

            nums1_left = nums1[i-1] if i > 0 else float('-inf') # nums1_left 為 nums1 切割線左邊的數字
            nums1_right = nums1[i] if i < m else float('inf')   # nums1_right 為 nums1 切割線右邊的數字
            nums2_left = nums2[j-1] if j > 0 else float('-inf') # nums2_left 為 nums2 切割線左邊的數字
            nums2_right = nums2[j] if j < n else float('inf')   # nums2_right 為 nums2 切割線右邊的數字

            if nums1_left <= nums2_right and nums2_left <= nums1_right: # 左半邊數字都 < 右半邊數字
                if (m + n) % 2 == 1:    # 數字總個數為奇數
                    return max(nums1_left, nums2_left)
                else:                   # 數字總個數為偶數
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:  # nums1 左邊數字太大，切割線範圍 right 往左移
                right = i - 1
            else:                           # nums1 右邊數字太小，切割線範圍 left 往右移
                left = i + 1
            
'''
Notes:
1. python 無窮大
    負無窮大: float('-inf')
        print(float('-inf')) -> -inf
        print(1 + float('-inf')) -> -inf
        
    正無窮大: float('inf')
        print(float('inf')) -> inf
        print(1 + float('inf')) -> inf

2. 此題解題思路參考:
     https://www.youtube.com/watch?v=wDBnBA82z1c&ab_channel=LeetCode%E5%8A%9B%E6%89%A3

'''