array = [
    ('바나나', 2)
    , ('사과', 5)
    , ('당근', 3)
]

# print(array)

def setting(data):
    return data[1]

print(
    sorted(array, key=setting, reverse=True)
)

print(
    sorted(array, key=lambda x:x[1], reverse=True)
)