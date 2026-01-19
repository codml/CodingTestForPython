n = int(input())
arr = [*map(int, input().split())]
dp = [1] * n
for idx, num in enumerate(arr):
    for j in range(idx):
        if arr[j] < num:
            dp[idx] = max(dp[idx], dp[j]+1)
print(max(dp))