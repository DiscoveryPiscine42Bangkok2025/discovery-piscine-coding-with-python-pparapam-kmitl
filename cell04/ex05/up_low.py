user = input("Input: ")
user1 = ""

for i in user:
    if i.isupper():
        user1 += i.lower()
    elif i.islower():
        user1 += i.upper()
    else:
        user1 += i

print(user1)