class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find the path (0,0)->(n-1,n-1) that has smallest max water level
        # in-place update
        n = len(grid)
        d = [(-1,0), (1,0), (0,-1), (0,1)]

        visited = [[False]*n for _ in range(n)]       
        queue = [(grid[0][0], 0, 0)]
        while queue:
            res, x, y = heapq.heappop(queue)
            if visited[x][y]:
                continue
            visited[x][y] = True
            if x == n-1 and y == n-1:
                return res
            
            for i in range(4):
                nei_x, nei_y = x+d[i][0], y+d[i][1]
                if 0 <= nei_x < n and 0 <= nei_y < n and not visited[nei_x][nei_y]:
                    heapq.heappush(queue, (max(res, grid[nei_x][nei_y]), nei_x, nei_y))
        return -1