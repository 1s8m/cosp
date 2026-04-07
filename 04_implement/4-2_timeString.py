n = int(input())

count = 0

# 00시 00분 00초부터~ 23시 59분 59초까지를 대상으로 함
for i in range(n+1): # n 시부터 
    for j in range(60):
        for k in range(60):
            if "3" in str(i)+str(j)+str(k):
                count += 1
print(count)