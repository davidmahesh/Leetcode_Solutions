class Solution:
    def asteroidsDestroyed(self, mass, asteroids):
        for a in sorted(asteroids):
            if mass < a:
                return False
            mass += a
        return True