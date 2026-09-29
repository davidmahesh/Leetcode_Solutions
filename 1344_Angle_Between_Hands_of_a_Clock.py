class Solution:
    def angleClock(self, hour, minutes):
        minute_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        diff = abs(minute_angle - hour_angle)
        return min(diff, 360 - diff)