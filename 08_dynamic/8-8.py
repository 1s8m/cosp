n, m = 3, 7
std_current_array = [2, 3, 5]

dp = [10001] * (m + 1) # 0 인덱스를 쓰지말고, 0 ~ 7까지 인덱스를 사용!

dp[0] = 0
for each_std in std_current_array:
    print(f'std_coin_{each_std}')
    for i in range(each_std, m+1):
        dp[i] = min(dp[i], dp[i-each_std] + 1)
        print(dp[i])

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])