# n, k = map(int, input().split())
# result = 0

# while n >= k:

#     while n % k != 0: # n 이 k 배수가 될 때까지 1씩 빼기!
#         n -= 1
#         result += 1
    
#     n //= k
#     result += 1

# while n > 1:
#     n -= 1
#     result += 1

# print(result)

n, k = map(int, input().split())
result = 0

while True:
    target_k_multiple = (n // k) * k
    result += n - target_k_multiple
    n = target_k_multiple

    if n < k: break # n 이 1이 되었을 경우,

    n //= k
    result += 1

result += n - 1
print(result)