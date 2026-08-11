class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        result = maxCount = 0

        for num in nums:
            count[num] += 1

            if maxCount < count[num]:
                result = num
                maxCount = count[num]
            
        return result