class Solution:
    @staticmethod
    def dist(point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        dist_matrix = []
        for i in range(len(points)):
            dists = {}
            for j in range(len(points)):
                p1 = points[i]
                p2 = points[j]
                dist_ = self.dist(p1, p2)
                if dist_ in dists:
                    dists[dist_] += 1
                else:
                    dists[dist_] = 1
            dist_matrix.append(dists)

        res = 0
        for dict_ in dist_matrix:
            for v in dict_.values():
                if v >= 2:
                    res += v * (v - 1)

        return res