# def factorial(n):
#     result = 1
#     for i in range(1, n+1): # 1에서 n 까지
#         result *= i
#     return result

# print(factorial(4))


def factorial(n):
    if n == 0 : return 1
    else : return n * factorial(n-1)

print(factorial(4))