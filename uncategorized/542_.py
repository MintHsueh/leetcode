# 542. 01 Matrix

from collections import deque

# Dynamic Programming??
# https://leetcode.com/problems/01-matrix/solutions/1369741/c-java-python-bfs-dp-solutions-with-picture-clean-concise-o-1-space/

class Solution:
    # BFS
    def updateMatrix_bfs(self, mat):
        m, n = len(mat), len(mat[0])
        
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = -1

        dir = [-1, 0, 1, 0, -1]
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dir[i], c + dir[i+1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        
        return mat
    
    # DP