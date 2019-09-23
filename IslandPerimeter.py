class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        print 'm: ', m
        n = len(grid[0])
        print 'n: ', n
        y = 0
        area, nb = 0, 0
        while y < m:
            print 'current y: ', y
            x = 0
            while x < n:
                print 'current x: ', x
                if grid[y][x] == 1:
                    area += 1
                    if y > 0 and grid[y-1][x] == 1:
                        nb += 1
                    if y < m-1 and grid[y+1][x] == 1:
                        nb += 1
                    if x > 0 and grid[y][x-1] == 1:
                        nb += 1
                    if x < n-1 and grid[y][x+1] == 1:
                        nb += 1
                x += 1
            y += 1
        print 'total area and neighbors: ', area, nb
        return area*4 - nb

island = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
s = Solution()
print s.islandPerimeter(island)
