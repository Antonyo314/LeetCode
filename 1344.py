class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(hour % 12 / 12 * 360 + minutes / (60 * 12) * 360 - minutes / 60 * 360)
        print(angle)
        if angle > 180:
            angle = 360 - angle
        return angle
