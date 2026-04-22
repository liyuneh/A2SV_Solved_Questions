class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mx = 0
        dxn = [(-1, 0), (1, 0), (0, -1), (0 , 1)]
        n , m = len(grid), len(grid[0])
        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            count = 1

            for x, y in dxn:
                count += dfs(row + x, col + y)

            return count
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    mx = max(mx, dfs(i, j))

        print(mx)
        return mx
            