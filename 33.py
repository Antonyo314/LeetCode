
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        if len(nums) == 1:
            if target in nums:
                return 0
            else:
                return -1

        while j - i > 1:
            t = (j - i) // 2 + i

            if nums[t] > nums[j]:
                i = t
            else:
                j = t

        k = i

        if k == 0:
            i = 0
            j = len(nums) - 1
            if nums[0] == target:
                return 0
        elif target >= nums[0]:
            i = 0
            j = k

        else:
            i = k + 1
            j = len(nums) - 1

        while j - i > 1:
            t = (j - i) // 2 + i
            if nums[t] < target:
                i = t
            else:
                j = t
        if nums[i] == target:
            return i
        elif nums[j] == target:
            return j
        else:
            return -1