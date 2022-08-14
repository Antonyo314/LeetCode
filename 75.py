class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for _ in range(len(nums)):
            for i, j in zip(range(len(nums)), range(1, len(nums))):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]