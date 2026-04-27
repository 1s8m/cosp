# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     else:
#         return fibo(x-1) + fibo(x-2)

# print(fibo(7))



# # caching, memoization (top-down)
# d = [0] * 100

# def fibo(x):
#     print(f'f({str(x)})', end=' ')
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]

# print(fibo(6))

# caching, memoization (bottom-down)
d = [0] * 100

d[1] = 1
d[2] = 1
n = 8

for i in range (3, (n+1)):
    d[i] = d[i-2] + d[i-1]

print(d[n])
