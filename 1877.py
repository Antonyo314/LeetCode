class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums) // 2
        a = nums[:n]
        b = nums[n:]
        b = b[::-1]

        max_ = a[0]

        for i in range(len(a)):
            if a[i] + b[i] > max_:
                max_ = a[i] + b[i]

        return max_
