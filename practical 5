def knapsack(W, val, wt):
    n = len(wt)

    dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):

            if wt[i - 1] <= j:
                pick = val[i - 1] + dp[i - 1][j - wt[i - 1]]
                not_pick = dp[i - 1][j]

                dp[i][j] = max(pick, not_pick)

            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


n = int(input("Enter number of items: "))

val = []
wt = []

for i in range(n):
    v = int(input("Enter value: "))
    w = int(input("Enter weight: "))

    val.append(v)
    wt.append(w)

W = int(input("Enter capacity: "))

print("Maximum value:", knapsack(W, val, wt))
