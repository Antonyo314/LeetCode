class Solution:
    @staticmethod
    def dist(x1, x2, y1, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]

        for point in points:
            t = []
            for point_ in points:
                x, y = point
                x_, y_ = point_
                t.append(self.dist(x, x_, y, y_))
            t.sort()
            if t[1] == 0:
                return False
            if not (t[0] == 0 and t[1] == t[2] and t[3] == 2 * t[1]):
                return False
        return True
