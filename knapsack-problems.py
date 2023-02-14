# ref: https://zxi.mytechroad.com/blog/sp/knapsack-problem/
from typing import List

w = [1,1,2,2]
v = [1,2,4,5]
W= 4

w2 = [1,2]
v2 = [2,5]
W2= 5
# 0-1 knapsack

def knapsack01(w: List[int], v: List[int], W: int) -> int:
    dp = [0] * (W+1)
    n = len(w)
    for i in range(n):
        for j in range(W, w[i]-1, -1):
            dp[j] = max(dp[j], dp[j-w[i]]+ v[i])
    return max(dp)

# unbounded knapsack
def knapsackUnbounded(w: List[int], v: List[int], W: int) -> int:
    dp = [0] * (W+1)
    n = len(w)
    for i in range(n):
        for j in range(w[i], W+1):
            dp[j] = max(dp[j], dp[j-w[i]]+ v[i])
    return max(dp)

# bounded knapsack


if __name__ == "__main__":
    print(knapsack01(w, v, W))
    print(knapsackUnbounded(w2, v2, W2))
