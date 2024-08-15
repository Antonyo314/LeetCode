class Solution:
    def a_k_b(self, point1, point2):
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]

        if x1 == x2:
            a = 0
            k = -1
            b = x1

        else:
            a = 1
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
        return a, k, b

    def on_line(self, point, a, k, b):
        if abs(a * point[1] - k * point[0] - b) < 0.000000001:
            return True
        else:
            return False

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        max_ = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a, k, b = self.a_k_b(points[i], points[j])
                res = 0
                for l in range(len(points)):
                    if self.on_line(points[l], a, k, b):
                        res += 1

                if res > max_:
                    max_ = res

        return max_