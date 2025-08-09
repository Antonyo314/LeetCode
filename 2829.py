class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        avoid = []

        for i in range(1, k):
            if i!=k-i:
                avoid.append(max(i, k - i))
        avoid = list(set(avoid))
        result_list = []
        t = 0
        while len(result_list) < n:
            t+=1
            while t in avoid:
                t+=1
            result_list.append(t)
        return sum(result_list)