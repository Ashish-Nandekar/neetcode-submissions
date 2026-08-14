class Solution:
    def merge(self, nums: List[int], low, mid, high) -> None:
        temp = []
        left = low
        right = mid + 1

        # Merge two sorted halves
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        # Remaining elements from left half
        while left <= mid:
            temp.append(nums[left])
            left += 1

        # Remaining elements from right half
        while right <= high:
            temp.append(nums[right])
            right += 1

        # Replace only the current range
        nums[low:high + 1] = temp

    def mergeSort(self, nums: List[int], low, high) -> None:
        if low >= high:
            return

        mid = low + (high - low) // 2

        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid + 1, high)

        self.merge(nums, low, mid, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums