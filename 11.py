class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_ = max(height)
        height_ = height.copy()
        height_.remove(max_)
        max_ = max(height_)
        max_square = 0

        for h in range(max_, 0, -1):
            i = 0
            j = len(height) - 1

            while height[i] < h:
                i += 1

            while height[j] < h:
                j -= 1

            max_square = max(max_square, h * (j - i))

        return max_square
