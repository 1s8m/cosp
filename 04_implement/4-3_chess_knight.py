input_data = input().lower()
# print(input_data)

x1 = ord(input_data[0]) - ord('a') + 1 # a가 1이 되도록 처리
x2 = int(input_data[1])

moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for move in moves:
    nx1 = x1 + move[0]
    nx2 = x2 + move[1]
    if nx1 > 0 and nx1 < 9 and nx2 > 0 and nx2 < 9:
        result += 1
        print(
            chr(nx2 -1 +ord('a')) + str(nx1)
        )

print(result)