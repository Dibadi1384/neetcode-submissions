class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        u,d=0, len(matrix)-1
        l,r=0, len(matrix[0])-1
        res=[]
        direc=1
        
        while u <= d and l <= r:
            if direc==1:
                #+1 includes r too
                for i in range(l,r+1,1):
                    res.append(matrix[u][i])
                u+=1
                for i in range(u,d+1,1):
                    res.append(matrix[i][r])
                r-=1
            else:
                #-1 include l too
                for i in range(r,l-1,-1):
                    res.append(matrix[d][i])
                d-=1
                for i in range(d,u-1,-1):
                    res.append(matrix[i][l])
                l+=1
                
            direc=direc*-1
        return res

               

        




        