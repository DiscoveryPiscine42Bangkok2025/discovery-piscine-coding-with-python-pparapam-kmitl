list = [2, 8, 9, 48, 8, 22, -12, 2]
list2 = []

for i in list :
    if i > 5:
        num = i + 2
        list2.append(num)
        num = set(list2)

print(f"Original array: {list}")
print(f"New array: {num}")