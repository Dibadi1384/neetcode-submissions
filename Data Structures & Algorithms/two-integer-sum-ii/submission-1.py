class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hp={}

        for i,n in enumerate(numbers):
            diff=target-n
            if diff in hp:
                return[hp[diff]+1, i+1]
            hp[n]=i

        