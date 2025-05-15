# 733. Flood Fill

from collections import deque
class Solution:
    # DFS
    # Time Complexity: O(mn)，最慘的狀況就是每一格都要填滿
    # Space Complexity: O(mn)，原因同上
    def floodFill_dfs(self, image, sr: int, sc: int, color: int):
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]
        
        def fill(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or image[r][c] != start_color or image[r][c] == color:
                return

            image[r][c] = color
            fill(r-1, c)
            fill(r+1, c)
            fill(r, c-1)
            fill(r, c+1)
        
        fill(sr, sc)
        return image

    # BFS
    # Time Complexity: O(mn)，最慘的狀況就是每一格都要填滿
    # Space Complexity: O(mn)，原因同上
    def floodFill_bfs(self, image, sr: int, sc: int, color: int):
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]

        q = deque([(sr, sc)])
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r < 0 or c < 0 or r >= m or c >= n or image[r][c] != start_color or image[r][c] == color:
                    continue
                image[r][c] = color
                q.append((r-1, c))
                q.append((r+1, c))
                q.append((r, c-1))
                q.append((r, c+1))
        
        return image

