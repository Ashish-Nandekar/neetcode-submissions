class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for num in nums:
            if num != val:
                temp.append(num)
            
        nums[:] = list(temp)

        return len(temp)
