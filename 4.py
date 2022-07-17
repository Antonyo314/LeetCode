class Solution:
    def quick_sort(self, arr):
        less, equal, greater = list(), list(), list()
        if len(arr) > 1:
            t = arr[0]
            for a in arr:
                if a < t:
                    less.append(a)
                elif a > t:
                    greater.append(a)
                else:
                    equal.append(a)
            return self.quick_sort(less) + equal + self.quick_sort(greater)
        else:
            return arr

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = self.quick_sort(nums)

        n = len(nums)
        if n % 2 == 0:
            return (nums[n // 2] + nums[n // 2 - 1]) / 2
        else:
            return nums[n//2]