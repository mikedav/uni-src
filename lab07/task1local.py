"""
IU7-15B Lab 7 
Task 1
1 3 2 2 
"""
data = list(map(int, input("Введите список через пробел: ").split()))

num_deleted = 0
i = 0

while i + num_deleted < len(data):
    if data[i + num_deleted] == 0:
        num_deleted += 1
    if i + num_deleted < len(data):
        data[i] = data[i + num_deleted]
    i += 1

data = data[:-num_deleted]


print(*data)
