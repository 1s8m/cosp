# n = int(input())
n = 4

# food_array = list(
#     map(int, input().split())
# )
food_array = [1, 3, 1, 5]


dp = [0] * len(food_array)

dp[0] = food_array[0]
dp[1] = max(food_array[0], food_array[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+food_array[i])

print([(idx, each) for idx, each in enumerate(dp)])
print(dp[-1])
