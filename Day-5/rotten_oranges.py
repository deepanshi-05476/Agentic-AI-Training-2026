from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])

        q = deque()
        fresh_count = 0

        # Store rotten oranges and count fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        # No fresh oranges already
        if fresh_count == 0:
            return 0

        minutes_passed = 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while q and fresh_count > 0:
            current_size = len(q)
            minutes_passed += 1

            for _ in range(current_size):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < m and 
                        0 <= nc < n and 
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh_count -= 1

        return minutes_passed if fresh_count == 0 else -1
