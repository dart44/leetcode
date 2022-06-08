import collections


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        
        def bfs(r, c):
            neighbors = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))
            
            while queue:
                row, col = queue.popleft()
                
                for nr, nc in neighbors:
                    r, c = row + nr, col + nc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))
        
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands+= 1
        return islands

# Test
def main():
    test = Solution()
    n = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    print(f'{test.numIslands(n)}')
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()