class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 4*x+ 2*y = tomatoSlices
        # x+y = cheeseSlices
        # y = cheeseSlices - x
        # 4*x + 2 * (cheeseSlices - x) = tomatoSlices
        # 4*x + 2 * (cheeseSlices - x) = tomatoSlices
        # 2*x = tomatoSlices - 2 * cheeseSlices

        # x = tomatoSlices/2 - cheeseSlices
        # y = cheeseSlices - x

        if tomatoSlices % 2 == 0:
            x = tomatoSlices / 2 - cheeseSlices
            y = cheeseSlices - x
            if x >= 0 and y >= 0:
                return [int(x), int(y)]
            else:
                return []
        else:
            return []
