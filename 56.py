class Solution:
    def qs(self, arr):
        if len(arr) <= 1:
            return arr

        t = arr[len(arr) // 1 - 1][0]

        s = list()
        e = list()
        b = list()

        for a in arr:
            if a[0] < t:
                s.append(a)
            elif a[0] == t:
                e.append(a)
            else:
                b.append(a)

        return self.qs(s) + e + self.qs(b)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = self.qs(intervals)

        changed = True
        while changed:
            changed = False
            for i in range(len(intervals) - 1):
                if intervals[i][1] >= intervals[i + 1][0]:
                    t = [intervals[i][0], max(intervals[i][1], intervals[i + 1][1])]
                    intervals[i] = t
                    intervals[i + 1] = t
                    changed = True
            new_intervals = [intervals[0]]
            for i in range(1, len(intervals)):
                if intervals[i] != intervals[i - 1]:
                    new_intervals.append(intervals[i])
            intervals = new_intervals
        return new_intervals

