class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k:
            i = nums.index(min(nums))
            nums[i] = -nums[i]
            k -= 1
        return sum(nums)
