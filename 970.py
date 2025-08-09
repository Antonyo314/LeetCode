class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x==1:
            x_ = [1]
        else:
            x_ = []
            a = 1
            while a < bound:
                x_.append(a)

                a *= x


        if y==1:
            y_ = [1]
        else:
            y_ = []
            b = 1
            while b < bound:
                y_.append(b)

                b *= y
        res = []
        for x in x_:
            for y in y_:
                if x + y <= bound:
                    res.append(x + y)

        return list(set(res))
