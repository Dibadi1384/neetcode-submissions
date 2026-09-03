
class DSU:
    def __init__(self, n):

        self.parent=list(range(n+1))
        self.size=[1]*(n+1)
        self.sizemax=0
        
    def find(self, n):
        if self.parent[n]!=n:
           n=self.find(self.parent[n])
        return self.parent[n]

    def union(self, u, v):
        pv=self.find(v)
        pu=self.find(u)

        if pv==pu:
            return False

        if self.size[pv]>=self.size[pu]:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
            if self.size[pv]>self.sizemax:
                self.sizemax=self.size[pv]
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
            if self.size[pu]>self.sizemax:
                self.sizemax=self.size[pu]
        
        return True
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows,cols=len(grid), len(grid[0])
        dsu=DSU(rows*cols)
        edge=0

        def index(r,c):
            return r*cols + c

        dirs=[(0,1),(0,-1),(1,0),(-1,0)]

        
        for r in range(rows):
            for c in range(cols):
                for dr,dc in dirs:
                    nr,nc=r+dr, c+dc
                    if grid[r][c]==1:
                        edge=1
                        if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]==0:
                            continue
                        dsu.union(index(r,c), index(nr,nc))
                        
        return max(edge,dsu.sizemax)

        