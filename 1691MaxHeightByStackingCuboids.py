from typing import List
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # rotate cube so that width<=length<=height
        for item in cuboids:
            item.sort()
        # sort by width, then length, then height
        cuboids = sorted(cuboids, key=lambda x: (x[0], x[1], x[2]))

        n = len(cuboids)
        dp = [0] * n
        # dp[i] to hold accumated height at each i
        for i, cube in enumerate(cuboids):
            dp[i] = cube[2]
            for j in range(i):
                if cube[1] >= cuboids[j][1] and cube[2] >= cuboids[j][2]:
                    dp[i] = max(dp[i], dp[j] + cube[2])

        return max(dp)
