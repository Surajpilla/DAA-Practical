#matrix
def matrix_chain(p, n):
    dp = [[0 for j in range(n)] for i in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = 999999

            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j]
                        + p[i - 1] * p[k] * p[j])

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n - 1]



n = int(input("Enter number of matrices: "))

p = []

print("Enter dimensions:")
for i in range(n + 1):
    x = int(input())
    p.append(x)

ans = matrix_chain(p, n)

print("Minimum number of multiplications:", ans)
