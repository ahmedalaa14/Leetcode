class Solution(object):
    def asteroidCollision(self, asteroids):
        n = len(asteroids)
        data = [None] * n
        head = -1

        for i in asteroids:
            if i > 0:
                head += 1
                data[head] = i
                continue
            else:
                alive = True
                while head >= 0 and data[head] > 0:
                    if data[head] > abs(i):
                        alive = False
                        break
                    elif data[head] == abs(i):
                        head -= 1
                        alive = False
                        break
                    head -= 1

                if alive:
                    head += 1
                    data[head] = i

        ans = data[:head + 1]
        return ans