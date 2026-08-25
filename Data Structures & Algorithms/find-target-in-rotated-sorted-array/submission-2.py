class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r=0,len(nums)-1

        while l<r:
            m=(r+l)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        p=l

        def bs(l: int, r:int)->int:
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return -1


        lh=bs(0,p-1)
        if lh!=-1:
            return lh
        return bs(p,len(nums)-1)

