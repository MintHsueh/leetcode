'''
118. pascal's triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''

class Solution:
    def generate(self, numRows):
        if numRows <= 0:
             return []
        elif numRows == 1:
             return [[1]]
        else:
            triangle = [[1]]
            for i in range(1, numRows):
                row_list = [1]
                for j in range(0, len(triangle[i-1])-1):
                    row_list.append(triangle[i-1][j] + triangle[i-1][j+1])
                row_list.append(1)
                triangle.append(row_list)
            return triangle

a = Solution().generate(6)
print(a)

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         finalNums=[]
#         finalNums.append([1])
#         for i in range(numRows-1):
#             newRow=[1]
#             for j in range(i):
#                 newRow.append(finalNums[i][j]+finalNums[i][j+1])
#             newRow.append(1)
#             finalNums.append(newRow)
#         return finalNums

# Solution().generate(2)
