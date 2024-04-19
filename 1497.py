class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = [a % k for a in arr]
        arr.sort()
        if arr.count(0) % 2 != 0:
            return False

        arr = [a for a in arr if a != 0]

        while len(arr) > 0:

            if arr[0] + arr[-1] == k:
                arr = arr[1:-1]
            else:
                return False
        return True