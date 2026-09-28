def coin_change(coins, amount):
    n = len(coins)

    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, amount + 1):

            if coins[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    print("\nDP Table:")

    for row in dp:
        print(row)

    return dp[n][amount]


coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))

ways = coin_change(coins, amount)

print("Number of ways:", ways)
