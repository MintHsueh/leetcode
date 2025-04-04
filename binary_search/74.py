# 74. Search a 2D Matrix
# Medium
# 2025/04/03

# Time Complexity: O(log m + log n) = O(log(m*n))
class Solution:
    # TC: O(log m + log n) = O(log(m*n)), SC: O(1)
    # Where m is the number of rows and n is the number of columns of matrix.
    def searchMatrix(self, matrix, target: int) -> bool:
        # 1st Binary Search: 檢查 target 有沒有在任一 row 頭跟尾的區間裡
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l  +  r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                row = m
                break           # 若有，則出迴圈，進行 2nd Binary Search
        else:                   # 若沒有，則 reurn False (記得 else, 否則繼續往下執行, row 會因沒定義而報錯)
            return False
        
        # 2nd Binary Search: 檢查 target 那一 row 裡
        l, r = 0, len(matrix[row])-1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1
        return False

# 待研究: 將 2D 視為 1D 做 Binary Search