# 36. Valid Sudoku
# Medium
# 2025/03/17

from collections import defaultdict

class Solution:
    # ***
    # Hash Set
    # TC: O(n^2), SC: O(n^2)
    def isValidSudoku_1(self, board) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or  
                    board[r][c] in boxes[(r//3, c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])
        
        return True

    # Brute Force
    # Time complexity: O(n^2) 
    # Space complexity: O(n^2)
    def isValidSudoku_2(self, board) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        #-------------------------------------
        # 檢查 3* 3 的 box 寫法 1
        def isValidBox(board, start_r, start_c):
            seen = set()
            for r in range(start_r, start_r + 3):
                for c in range(start_c, start_c + 3):
                    if board[r][c] != ".":
                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c])
            return True

        for i in [0, 3, 6]: # range(0, 9, 3)
            for j in [0, 3, 6]:
                if not isValidBox(board, i, j):
                    return False
                
        # 檢查 3* 3 的 box 寫法 2
        boxes = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (r//3, c//3) in boxes:
                    if board[r][c] in boxes[(r//3, c//3)]:
                        return False
                    else: 
                        boxes[(r//3, c//3)].add(board[r][c])
                else:
                    boxes[(r//3, c//3)] = set()
                    boxes[(r//3, c//3)].add(board[r][c])
        #-------------------------------------
        return True 

'''
Notes:

1. from collections import defaultdict

2. defaultdict(set) # 預設存在任何的 key, 預設每個 key 的 value 是 set() 
    → 就不用檢查這個 key 值是否存在

3. 參數可以是:
    dict1 = defaultdict(int)    # 預設 value: 0
    dict2 = defaultdict(set)    # 預設 value: set()
    dict3 = defaultdict(str)    # 預設 value: ""
    dict4 = defaultdict(list)   # 預設 value: []

4. eg.
    boxes = defaultdict(set) 
    boxes[(2, 1)].add(5)
    print(boxes[1]) # set()
    print(boxes[(2, 1)])    # {5}

5. 字典的 key 可以同時存在不同 type
    a = {1:2, (3,4):5} # 
    print(a[1])    # 2
    print(a[(3,4)]) # 5

source: https://hjp-muser.github.io/2020/04/21/python%E4%B8%ADdefaultdict%E7%94%A8%E6%B3%95%E8%AF%A6%E8%A7%A3/

'''
