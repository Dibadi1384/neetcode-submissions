class DSU:
    def __init__(self,n):
        self.Parent=list(range(n+1))
        self.Size=[1]*(n+1)

    def find(self,node):
        if self.Parent[node] != node:
            self.Parent[node]=self.find(self.Parent[node])
        return self.Parent[node]

    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)

        if pu==pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu]+=self.Size[pv]
            self.Parent[pv]=pu
        else:
            self.Size[pv]+=self.Size[pu]
            self.Parent[pu]=pv

        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid), len(grid[0])

        dsu=DSU(rows*cols)

        def index(r,c):
            return r*cols+c

        directions=[(1,0), (-1,0), (0,1), (0,-1)]
        island=0

        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == "1":
                    island +=1
                    for dr, dc in directions:
                        nr,nc=r+dr,c+dc

                        if (nr<0 or nc<0  or nr>=rows or nc>=cols or grid[nr][nc]=="0"):
                            continue
                        if dsu.union(index(r, c), index(nr, nc)):
                            island -= 1
        return island

    




