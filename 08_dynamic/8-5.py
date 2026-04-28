x = int(input())

d = [0] * 30001

for i in range(2, x+1): # x+1-(1) 까지, 0 은 대상 아니고, 1 은 결과
    
    # 1 빼기
    d[i] = d[i-1] + 1

    # 2 나누기
    if i % 2 == 0: 
        d[i] = min(d[i], d[i // 2] + 1)

    # 3 나누기
    if i % 3 == 0: 
        d[i] = min(d[i], d[i // 3] + 1)

    # 5 나누기
    if i % 5 == 0: 
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
print([(idx, each) for idx, each in enumerate(d) if idx <= x])