class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        order = sorted(range(n), key=lambda i: positions[i])
        stack = []
        alive = healths[:]
        for i in order:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and alive[i] > 0:
                    top = stack[-1]
                    if alive[top] > alive[i]:
                        alive[top] -= 1
                        alive[i] = 0
                    elif alive[top] < alive[i]:
                        alive[i] -= 1
                        alive[top] = 0
                        stack.pop()
                    else:
                        alive[top] = 0
                        alive[i] = 0
                        stack.pop()
        return [alive[i] for i in range(n) if alive[i] > 0]