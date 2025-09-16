num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

num3 = num1 * num2

if num3 > 0:
    print(num3, "The result is positive")
elif num3 < 0:
    print(num3, "The result is negative.")
else:
    print(num3, "The result is positive and negative.")